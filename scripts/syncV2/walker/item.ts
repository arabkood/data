import { v4 as uuidv4 } from "uuid";
import yaml from "js-yaml";
import path from "node:path";
import { items, type Item, type ItemPartial } from "../models";
import { createInsertSchema } from "drizzle-zod";
import { ROOT } from "../config";

const schema = createInsertSchema(items);

function getSlugAndPosition(itemDir: string) {
  if (!itemDir) {
    throw new Error("Item dir cannot be empty or null");
  }

  const itemName = path.basename(itemDir);
  const parts = itemName.split("_", 2);

  let cleanName: string;
  let position = 0;

  if (parts.length > 1) {
    const positionNum = parseInt(parts[0], 10);
    position = isNaN(positionNum) ? 0 : positionNum;
    cleanName = parts[1];
  } else {
    cleanName = parts[0];
  }

  if (!cleanName || cleanName.trim() === "") {
    throw new Error(
      `Invalid item name in path: ${itemDir}. Expected format: "[number]_[name]" but got: "${itemName}"`,
    );
  }

  return {
    slug: cleanName.trim(),
    position,
  };
}

// we'll need this later
export async function enrichItem(
  moduleId: string,
  sourcePath: string,
): Promise<Item> {
  const yamlPath = path.join(sourcePath, "+item.yml");
  const fields = yaml.load(await Bun.file(yamlPath).text()) as ItemPartial;

  const enriched = { ...fields };
  let changed = false;

  const { slug, position } = getSlugAndPosition(sourcePath);
  const s3Path = path.relative(path.join(ROOT, "topics"), sourcePath);

  if (!enriched.id) {
    enriched.id = uuidv4();
    changed = true;
  }
  if (!enriched.created_at) {
    enriched.created_at = new Date();
    changed = true;
  }
  if (enriched.module_id !== moduleId) {
    enriched.module_id = moduleId;
    changed = true;
  }
  if (enriched.slug !== slug) {
    enriched.slug = slug;
    changed = true;
  }
  if (enriched.position !== position) {
    enriched.position = position;
    changed = true;
  }
  if (enriched.s3_path !== s3Path) {
    enriched.s3_path = s3Path;
    changed = true;
  }
  if (!enriched.updated_at) {
    changed = true;
  }
  if (changed) {
    enriched.updated_at = new Date();
  }

  const finalItem = (await schema.parseAsync(enriched).catch((error) => {
    throw new Error(`Validation failed for ${yamlPath}:\n${error.message}`);
  })) as Item;

  if (changed) {
    await Bun.write(yamlPath, yaml.dump(finalItem).trim());
  }

  return finalItem as Item;
}

export async function hashItem(sourcePath: string): Promise<[string, string]> {
  const yamlPath = path.join(sourcePath, "+item.yml");
  const partialItem = yaml.load(await Bun.file(yamlPath).text()) as ItemPartial;

  const finalItem = (await schema.parseAsync(partialItem).catch((error) => {
    throw new Error(`Validation failed for ${yamlPath}:\n${error.message}`);
  })) as Item;

  const hasher = new Bun.CryptoHasher("sha256");
  hasher.update(JSON.stringify(finalItem));
  const hash = hasher.digest("hex");

  return [finalItem.id, hash];
}
