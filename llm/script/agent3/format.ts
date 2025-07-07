import { mkdir, readdir, stat } from "node:fs/promises";
import { join, normalize } from "node:path";

const path = (...parts: string[]) => normalize(join(import.meta.dir, ...parts));

async function format() {
  const roadmapName = "General JavaScript For Beginners";

  const dist = path("./output/final/", roadmapName.replaceAll(" ", "_"));

  await mkdir(dist, { recursive: true });

  const failed: string[] = [];
  for (let index = 0; index <= 7; index++) {
    const modulePath = path(
      "./output/roadmaps/javascript/",
      roadmapName.replaceAll(" ", "_"),
      String(index),
      "ar",
    );
    const module = await Bun.file(
      path(
        "./output/roadmaps/javascript/",
        roadmapName.replaceAll(" ", "_"),
        String(index) + ".json",
      ),
    ).json();

    const modDist = join(dist, String(index).padStart(3, "0"));
    await mkdir(modDist, {
      recursive: true,
    });

    const files = await readdir(modulePath);
    await Promise.all(
      files.map(async (f) => {
        const fullpath = join(modulePath, f);
        const s = await stat(fullpath);
        if (s.isFile()) {
          const file = await Bun.file(fullpath).json();
          await mkdir(join(modDist, file.metadata.slug, "lesson"), {
            recursive: true,
          });
          const yamlContent = Object.entries(file.metadata)
            .map(([key, value]) => `${key}: ${JSON.stringify(value)}`)
            .join("\n");
          await Bun.write(
            join(modDist, file.metadata.slug, "+item.yml"),
            yamlContent,
          );
          for (const one of file.files) {
            const fin = join(modDist, file.metadata.slug, "lesson", one.name);
            try {
              await Bun.write(fin, one.content);
              console.log(`✅ Created: ${fin}`);
            } catch {
              failed.push(fin);
            }
          }
        }
      }),
    );
  }

  if (failed.length) {
    console.log("The following failed to copy: ");
    console.log(failed.join("\n"));
  }
}

format();
