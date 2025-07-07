import { ChatPromptTemplate } from "@langchain/core/prompts";
import { LLMRoadmaper } from "../config";
import { z } from "zod";
import { mkdir } from "node:fs/promises";
import { join, normalize } from "node:path";

const moduleSchema = z.array(
  z.object({
    title: z.string().describe("item title"),
    new_concept: z.array(z.string()).describe("main technical concept"),
    builds_on: z.array(z.string()).describe("concepts from old items used"),
    narrative_hook: z.string().describe("one sentence"),
  }),
);
const trackSchema = z.array(
  z.object({
    title: z.string().describe("module title"),
    goal: z.string().describe("module goal"),
    concepts_covered: z.array(z.string()).describe("main technical concepts"),
  }),
);

const path = (...parts: string[]) => normalize(join(import.meta.dir, ...parts));

export class RoadMapper {
  private llm: ReturnType<typeof LLMRoadmaper>;
  public docs: {
    platform: string;
    trackGenerator: string;
    moduleGenerator: string;
    roadmapGuidelines: string;
  };

  constructor() {
    this.llm = LLMRoadmaper();
  }

  async loadDocs() {
    this.docs = {
      platform: await Bun.file(path("../docs/our-platform.md")).text(),
      trackGenerator: await Bun.file(
        path("./docs/prompt-track-generator.md"),
      ).text(),
      moduleGenerator: await Bun.file(
        path("./docs/prompt-module-generator.md"),
      ).text(),
      roadmapGuidelines: await Bun.file(
        path("./docs/roadmap-guidelines.md"),
      ).text(),
    };
  }

  async generateModule(index: number, name: string) {
    console.log(`Starting module generation`);

    const trackPath = path("../output/roadmaps/javascript/", name);
    const roadmapPath = join(trackPath, "./track.json");

    const roadmap = await Bun.file(roadmapPath).json();

    // Load roadmap and style guide
    const template = `
---
${this.docs.platform}
---
${this.docs.roadmapGuidelines}
---
${this.docs.moduleGenerator}
---
`;

    const prompt = ChatPromptTemplate.fromTemplate(template, {
      templateFormat: "mustache",
    });

    const structuredLLM = this.llm.withStructuredOutput(moduleSchema);
    const chain = prompt.pipe(structuredLLM);

    console.log("Generating a module...");

    const result = await chain.invoke({
      roadmap: JSON.stringify(roadmap, null, 2),
      module: JSON.stringify(roadmap[index], null, 2),
      target: "Absolute beginners with no prior programming experience.",
    });

    console.log(result);

    await mkdir(trackPath, { recursive: true });
    await Bun.write(
      join(trackPath, index + ".json"),
      JSON.stringify(result, null, 2),
    );

    return result;
  }

  async generateTrack(roadmapName: string) {
    console.log(`Starting track generation`);

    // Load roadmap and style guide
    const template = `
---
${this.docs.platform}
---
${this.docs.roadmapGuidelines}
---
${this.docs.trackGenerator}
---
`;

    const prompt = ChatPromptTemplate.fromTemplate(template, {
      templateFormat: "mustache",
    });

    const structuredLLM = this.llm.withStructuredOutput(trackSchema);
    const chain = prompt.pipe(structuredLLM);

    console.log("Generating a track...");

    const result = await chain.invoke({
      topic: "javascript",
      roadmap: roadmapName,
      target: "Absolute beginners with no prior programming experience.",
      goal: "the user should be able to understand and use all important concepts from javascript (browser not included). The user should learn how to javascript as a general programming language to build script that can do anything.",
    });

    console.log(result);

    await mkdir(path("../output/roadmaps/javascript/"), { recursive: true });
    await Bun.write(
      path(
        "../output/roadmaps/javascript/",
        roadmapName.replaceAll(" ", "_"),
        "track.json",
      ),
      JSON.stringify(result, null, 2),
    );

    return result;
  }
}
