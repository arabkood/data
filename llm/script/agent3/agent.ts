import { ChatPromptTemplate } from "@langchain/core/prompts";
import { LLM, PATHS } from "./config";
import { saveResultsToDisk } from "./save";
import { type RoadmapItem } from "./types";
import * as fs from "node:fs";

const LESSON_GENERATION_PROMPT = `
You are an elite AI curriculum architect and senior instructional designer. Your expertise lies in applying principles of cognitive psychology and gamification to create highly engaging and effective programming lessons in Arabic.

You will generate multiple, distinct, multi-file lesson variants based on the provided information.

**Inputs:**
- **Target Lesson**: {lessonTitle}
- **Number of Variants**: {numberOfVariants}
- **Style Guide**: {styleGuide}

**Your Task:**
Generate exactly {numberOfVariants} unique lesson variants. Each variant should implement psychology-first design principles:

**File Requirements:**
1. Each variant must be a complete, self-contained lesson
2. Use a mix of .md (explanations) and .yml (quizzes) files
3. Number files sequentially: "01_intro.md", "02_quiz.yml", etc.
4. Follow ALL rules in the style guide strictly
5. Write all content in Arabic as specified in the style guide
6. For .yml files, use this structure:
   \`\`\`yaml
   type: "quiz"
   lang: "javascript"
   question: |
     ...
   code: |
     ...
   solution: 0
   options: [...]
   explanation: |
     ...
   \`\`\`

**Metadata Requirements:**
Each lesson variant must include a \`metadata\` object with the following fields:
- \`title\`: A clear, concise Arabic title for the lesson
- \`blurb\`: A short descriptive summary of the lesson (in Arabic)
- \`premium_only\`: \`true\` or \`false\` depending on access level
- \`difficulty\`: One of: \`easy\`, \`medium\`, or \`hard\`
- \`base_xp\`: An integer representing the XP reward between 500 and 3000
- \`type\`: Always set to \`lesson\`
- \`slug\`: A URL-friendly identifier for the lesson (lowercase, no spaces)

**Output Format:**
Return ONLY a JSON object with this exact structure:
{{
  "lessonVariants": [
    {{
      "variantNumber": 1,
      "metadata": {{
        "title": "...",
        "blurb": "...",
        "premium_only": false,
        "difficulty": "easy", // easy, medium, hard
        "base_xp": 500, // between 500 and 3000
        "type": "lesson",
        "slug": "..."
      }},
      "files": [
        {{
          "filename": "01_introduction.md",
          "content": "# Content here..."
        }},
        {{
          "filename": "02_quiz.yml",
          "content": "type: \\"quiz\\"\\nlang: \\"javascript\\"\\n..."
        }}
      ]
    }}
  ]
}}

Generate the lessons now:
`;

export class LessonGenerator {
  private llm: ReturnType<typeof LLM>;

  constructor() {
    this.llm = LLM();
  }

  async generateLessons(targetLessonId: number, numberOfVariants: number) {
    console.log(`Starting lesson generation for ID: ${targetLessonId}`);

    // Load roadmap and style guide
    const roadmapData: RoadmapItem[] = JSON.parse(
      fs.readFileSync(PATHS.roadmap, "utf-8"),
    );
    const styleGuideContent = fs.readFileSync(PATHS.styleguide, "utf-8");

    // Find target lesson
    const targetLesson = roadmapData.find(
      (lesson) => lesson.id === targetLessonId,
    );
    if (!targetLesson) {
      throw new Error(`Lesson with ID ${targetLessonId} not found in roadmap`);
    }

    console.log(`Found lesson: ${targetLesson.title}`);

    // Create prompt
    const prompt = ChatPromptTemplate.fromTemplate(LESSON_GENERATION_PROMPT);

    // Generate lessons with structured output
    // const structuredLLM = this.llm.withStructuredOutput(finalAnswerSchema);
    const chain = prompt.pipe(this.llm);

    console.log("Generating lesson variants...");
    const result = await chain.invoke({
      lessonTitle: targetLesson.title,
      numberOfVariants: numberOfVariants,
      styleGuide: styleGuideContent,
    });
    console.log(result);

    // Save results
    try {
      saveResultsToDisk(result.content.toString(), targetLessonId);
    } catch (error) {
      console.error("Error saving results:", error);
    }

    return result;
  }
}
