import { mkdir } from "node:fs/promises";
import files from "./file.json";

// Create the "example" directory if it doesn't exist
await mkdir("example", { recursive: true });

// Write each file
for (const file of files) {
  await Bun.write(`example/${file.name}`, file.content);
  console.log(`✅ Created: example/${file.name}`);
}
