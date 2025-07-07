import * as fs from "node:fs";
import * as path from "node:path";
/**
 * Takes the agent's final JSON output and writes the lesson files to disk.
 */
export function saveResultsToDisk(texto: string, lessonId: number) {
  let text = texto.trim();
  // 1. Define the base output directory to keep things organized.
  const baseOutputDir = path.join(process.cwd(), "output");
  // 2. Ensure the base output directory exists.
  if (!fs.existsSync(baseOutputDir)) {
    fs.mkdirSync(baseOutputDir);
  }
  console.log("\n--- Writing lesson variants to disk ---");
  // Remove only the first ```json from the start
  if (text.startsWith("```json")) {
    text = text.slice(7); // Remove 7 characters (length of "```json")
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
  console.log(jsonData);

  // 3. Loop through each generated variant in the JSON data.
  jsonData.lessonVariants.forEach((variant: any, index: number) => {
    // Use the variantNumber from the JSON, or the array index as a fallback.
    const variantNumber = variant.variantNumber || index + 1;
    const slug = variant.metadata.slug || "variant";
    const lessonDirName = `${lessonId.toString().padStart(3, "0")}_${slug}-${variantNumber}`;
    const lessonDirPath = path.join(baseOutputDir, lessonDirName);

    // 4. Create the lesson directory for this variant.
    fs.mkdirSync(lessonDirPath, { recursive: true });
    console.log(`Created lesson directory: ${lessonDirPath}`);

    // 5. Write the metadata to +item.yml
    if (variant.metadata) {
      const metadataPath = path.join(lessonDirPath, "+item.yml");
      // Convert metadata object to YAML format (simple key-value pairs)
      const yamlContent = Object.entries(variant.metadata)
        .map(([key, value]) => `${key}: ${JSON.stringify(value)}`)
        .join("\n");
      fs.writeFileSync(metadataPath, yamlContent);
      console.log(`  └─ Wrote metadata: +item.yml`);
    }

    // 6. Write the files from variant.files
    if (variant.files && Array.isArray(variant.files)) {
      variant.files.forEach((file: { filename: string; content: string }) => {
        if (file.filename && typeof file.content === "string") {
          const filePath = path.join(lessonDirPath, "lesson", file.filename);
          fs.mkdirSync(path.join(lessonDirPath, "lesson"), { recursive: true });
          // 7. Write the file's content to the disk.
          fs.writeFileSync(filePath, file.content);
          console.log(`  └─ Wrote file: ${file.filename}`);
        }
      });
    }
  });

  console.log("\n✅ All files written successfully!");
}
