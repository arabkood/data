import { z } from "zod";

export const fileSchema = z.object({
  filename: z
    .string()
    .describe("The name of the file, e.g., '01_intro.md' or '02_quiz.yml'"),
  content: z.string().describe("The complete, raw content of the file."),
});

export const metadataSchema = z.object({
  title: z.string().describe("Arabic title of the lesson"),
  blurb: z
    .string()
    .describe("A short descriptive summary of the lesson in Arabic"),
  premium_only: z
    .boolean()
    .describe("Whether this lesson is restricted to premium users"),
  difficulty: z
    .enum(["easy", "medium", "hard"])
    .describe("Difficulty level of the lesson"),
  base_xp: z.number().describe("Base XP rewarded for completing the lesson"),
  type: z.literal("lesson").describe("Content type, always 'lesson'"),
  slug: z.string().describe("URL-friendly identifier for the lesson"),
});

export const lessonVariantSchema = z.object({
  variantNumber: z
    .number()
    .describe("The sequential number for this lesson variant"),
  metadata: metadataSchema.describe(
    "Metadata information for the lesson variant",
  ),
  files: z
    .array(fileSchema)
    .describe("An array of all file objects that make up this lesson variant"),
});

export const finalAnswerSchema = z.object({
  lessonVariants: z
    .array(lessonVariantSchema)
    .describe("An array containing all the generated lesson variants"),
});

export type RoadmapItem = {
  id: number;
  title: string;
  keywords?: string[]; // New field for RAG keywords
  [key: string]: any;
};
