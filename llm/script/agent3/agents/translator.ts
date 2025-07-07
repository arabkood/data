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

export class Translator {
  private llm: ReturnType<typeof LLM>;
  public docs: {
    platform: string;
    translator: string;
    contentStyle: string;
    translationGuide: string;
  };

  constructor() {
    this.llm = LLM();
  }

  async loadDocs() {
    this.docs = {
      platform: await Bun.file(path("../docs/our-platform-ar.md")).text(),
      translator: await Bun.file(path("./docs/prompt-translate.md")).text(),
      contentStyle: await Bun.file(path("../docs/content-style.md")).text(),
      translationGuide: await Bun.file(
        path("./docs/translation-guidelines.md"),
      ).text(),
    };
  }

  async translateLesson(
    itemName: string,
    moduleIndex: number,
    roadmapName: string,
  ) {
    console.log(`Starting lesson translation`);

    const trackPath = path("../output/roadmaps/javascript/", roadmapName);
    const itemsPath = path(
      "../output/roadmaps/javascript/",
      roadmapName,
      String(moduleIndex),
    );
    const item = await Bun.file(join(itemsPath, itemName)).json();

    const distPath = path(
      "../output/roadmaps/javascript/",
      roadmapName,
      String(moduleIndex),
      "ar/",
    );

    // Load roadmap and style guide
    const template = `
---
${this.docs.platform}
---
${this.docs.contentStyle}
---
${this.docs.translationGuide}
---
${this.docs.translator}
---
`;

    const prompt = ChatPromptTemplate.fromTemplate(template, {
      templateFormat: "mustache",
    });

    // const structuredLLM = this.llm.withStructuredOutput(lessonSchema);
    const chain = prompt.pipe(this.llm);

    console.log("Translating a lesson...");

    const result = await chain.invoke({
      item: JSON.stringify(item, null, 2),
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
