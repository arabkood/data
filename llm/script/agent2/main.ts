import { LessonGenerator } from "./agent";

async function main() {
  try {
    const generator = new LessonGenerator();

    const targetLessonId = Number(process.env.TARGET_LESSON || 0);
    const numberOfVariants = Number(process.env.VARIANTS || 2);

    console.log(`Target Lesson ID: ${targetLessonId}`);
    console.log(`Number of Variants: ${numberOfVariants}`);

    const result = await generator.generateLessons(
      targetLessonId,
      numberOfVariants,
    );

    console.log("\n✅ Lesson generation completed successfully!");
  } catch (error) {
    console.error("❌ Error during lesson generation:", error);
    process.exit(1);
  }
}

main();
