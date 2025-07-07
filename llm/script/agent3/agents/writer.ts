import { join, normalize } from "node:path";
import { z } from "zod";
import { LLM } from "../config";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { mkdir } from "node:fs/promises";

export const lessonSchema = z.object({
  metadata: z
    .object({
      title: z.string().describe("title of the lesson"),
      blurb: z.string().describe("A short descriptive summary of the lesson"),
      difficulty: z
        .string()
        .describe("Difficulty level of the lesson, can be easy, hard, medium"),
      base_xp: z
        .number()
        .describe("Base XP rewarded for completing the lesson"),
      type: z.string().describe("Content type, always 'lesson'"),
      slug: z
        .string()
        .describe(
          "URL-friendly identifier for the lesson, without the track name, focused on lesson name only",
        ),
    })
    .describe("Metadata information for the lesson variant"),
  files: z
    .array(
      z.object({
        filename: z
          .string()
          .describe(
            "The name of the file, e.g., '01_lesson.md' or '02_quiz.yml'",
          ),
        content: z.string().describe("The complete, raw content of the file."),
      }),
    )
    .describe("An array of all file objects that make up this lesson variant"),
});

const path = (...parts: string[]) => normalize(join(import.meta.dir, ...parts));

export class Writer {
  private llm: ReturnType<typeof LLM>;
  public docs: {
    platform: string;
    lessonGenerator: string;
    contentStyle: string;
  };

  constructor() {
    this.llm = LLM();
  }

  async loadDocs() {
    this.docs = {
      platform: await Bun.file(path("../docs/our-platform.md")).text(),
      lessonGenerator: await Bun.file(
        path("./docs/prompt-lesson-generator.md"),
      ).text(),
      contentStyle: await Bun.file(path("../docs/content-style.md")).text(),
    };
  }

  async generateLesson(
    itemIndex: number,
    moduleIndex: number,
    roadmapName: string,
  ) {
    console.log(`Starting lesson generation`);

    const trackPath = path("../output/roadmaps/javascript/", roadmapName);
    const modulePath = path(
      "../output/roadmaps/javascript/",
      roadmapName,
      String(moduleIndex) + ".json",
    );
    const roadmapPath = join(trackPath, "./track.json");
    const roadmap = await Bun.file(roadmapPath).json();
    const module = await Bun.file(modulePath).json();

    const learnedConcepts: Set<string> = new Set([]);
    roadmap.forEach((m, i) => {
      if (i >= moduleIndex) {
        return;
      }
      if (typeof m.concepts_covered === "string") {
        learnedConcepts.add(m.concepts_covered as string);
      }
    });
    module.forEach((l, i) => {
      if (i >= itemIndex) {
        return;
      }
      l.new_concept.forEach((c) => {
        if (typeof c === "string") {
          learnedConcepts.add(c);
        }
      });
    });

    const currentItem = module[itemIndex];
    if (!currentItem) {
      throw "no current item: " + itemIndex;
    }

    const distPath = path(
      "../output/roadmaps/javascript/",
      roadmapName,
      String(moduleIndex),
    );

    // Load roadmap and style guide
    const template = `
---
${this.docs.platform}
---
${this.docs.contentStyle}
---
${this.docs.lessonGenerator}
---
`;

    const prompt = ChatPromptTemplate.fromTemplate(template, {
      templateFormat: "mustache",
    });

    // const structuredLLM = this.llm.withStructuredOutput(lessonSchema);
    const chain = prompt.pipe(this.llm);

    console.log("Generating a module...");

    const result = await chain.invoke({
      learned: [...learnedConcepts].join(", "),
      module: JSON.stringify(module, null, 2),
      lesson: JSON.stringify(currentItem, null, 2),
      target: "Absolute beginners with no prior programming experience.",
    });

    console.log(result.content);
    let text = result.content.toString();
    // Remove only the first ```json from the start
    if (text.startsWith("```json")) {
      text = text.slice(7);
    }
    // Remove only the first ``` from the end
    const closingFenceIndex = text.lastIndexOf("```");
    if (
      closingFenceIndex !== -1 &&
      closingFenceIndex + 3 === text.trimEnd().length
    ) {
      text = text.slice(0, closingFenceIndex);
    }

    const jsonData = JSON.parse(text);

    await mkdir(distPath, { recursive: true });
    await Bun.write(
      join(distPath, jsonData.metadata.slug + ".json"),
      JSON.stringify(jsonData, null, 2),
    );

    return result;
  }
}
