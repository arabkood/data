import { v4 as uuidv4 } from "uuid";
import yaml from "js-yaml";
import path from "node:path";
import { modules, type Module, type ModulePartial } from "../models";
import { createInsertSchema } from "drizzle-zod";

const schema = createInsertSchema(modules);

function extractModulePosition(moduleDir: string): number {
  if (!moduleDir) {
    return 0;
  }

  const moduleName = path.basename(moduleDir);
  const parts = moduleName.split("_", 2);
  const positionStr = parts[0];
  const position = parseInt(positionStr, 10);

  return isNaN(position) ? 0 : position;
}

// we'll need this later
export async function enrichModule(
  trackId: string,
  sourcePath: string,
): Promise<Module> {
  const yamlPath = path.join(sourcePath, "+module.yml");
  const fields = yaml.load(await Bun.file(yamlPath).text()) as ModulePartial;

  const enriched = { ...fields };
  let changed = false;

  const position = extractModulePosition(path.dirname(yamlPath));

  if (!enriched.id) {
    enriched.id = uuidv4();
    changed = true;
  }
  if (!enriched.created_at) {
    enriched.created_at = new Date();
    changed = true;
  }
  if (enriched.track_id !== trackId) {
    enriched.track_id = trackId;
    changed = true;
  }
  if (enriched.position !== position) {
    enriched.position = position;
    changed = true;
  }
  if (!enriched.updated_at) {
    changed = true;
  }
  if (changed) {
    enriched.updated_at = new Date();
  }

  const finalModule = (await schema.parseAsync(enriched).catch((error) => {
    throw new Error(`Validation failed for ${yamlPath}:\n${error.message}`);
  })) as Module;

  if (changed) {
    await Bun.write(yamlPath, yaml.dump(finalModule).trim());
  }

  return finalModule as Module;
}

export async function hashModule(
  sourcePath: string,
): Promise<[string, string]> {
  const yamlPath = path.join(sourcePath, "+module.yml");
  const partialModule = yaml.load(
    await Bun.file(yamlPath).text(),
  ) as ModulePartial;

  const finalModule = (await schema.parseAsync(partialModule).catch((error) => {
    throw new Error(`Validation failed for ${yamlPath}:\n${error.message}`);
  })) as Module;

  const hasher = new Bun.CryptoHasher("sha256");
  hasher.update(JSON.stringify(finalModule));
  const hash = hasher.digest("hex");

  return [finalModule.id, hash];
}
