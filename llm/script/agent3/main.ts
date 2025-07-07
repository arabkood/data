import { join, normalize } from "node:path";
import { RoadMapper } from "./agents/roadmaper";
import { Writer } from "./agents/writer";
import { Translator } from "./agents/translator";
import { readdir, stat } from "node:fs/promises";

const path = (...parts: string[]) => normalize(join(import.meta.dir, ...parts));

async function main() {
  try {
    const roadmaper = new RoadMapper();
    const writer = new Writer();
    const translator = new Translator();

    await roadmaper.loadDocs();
    await writer.loadDocs();
    await translator.loadDocs();

    const roadmapName = "General JavaScript For Beginners";

    // await roadmaper.generateTrack(roadmapName);
    //
    // if (!process.env.MODULE_INDEX) {
    //   throw "process.env.MODULE_INDEX";
    // }
    // await roadmaper.generateModule(
    //   parseInt(process.env.MODULE_INDEX),
    //   roadmapName.replaceAll(" ", "_"),
    // );

    // for (let index = 7; index <= 7; index++) {
    //   const modulePath = path(
    //     "./output/roadmaps/javascript/",
    //     roadmapName.replaceAll(" ", "_"),
    //     String(index) + ".json",
    //   );
    //   const module = await Bun.file(modulePath).json();
    //   for (let ii = 0; ii < module.length; ii++) {
    //     await writer.generateLesson(
    //       ii,
    //       index,
    //       roadmapName.replaceAll(" ", "_"),
    //     );
    //   }
    // }

    for (let index = 0; index <= 7; index++) {
      const modulePath = path(
        "./output/roadmaps/javascript/",
        roadmapName.replaceAll(" ", "_"),
        String(index),
      );
      const files = await readdir(modulePath);

      await Promise.all(
        files.map(async (f) => {
          const fullpath = join(modulePath, f);
          const s = await stat(fullpath);
          if (s.isFile()) {
            await translator.translateLesson(
              f,
              index,
              roadmapName.replaceAll(" ", "_"),
            );
          }
        }),
      );
    }

    console.log("\n✅ Track generation completed successfully!");
  } catch (error) {
    console.error("❌ Error during Track generation:", error);
    process.exit(1);
  }
}

main();
