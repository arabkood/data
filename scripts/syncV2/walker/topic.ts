import { v4 as uuidv4 } from "uuid";
import yaml from "js-yaml";
import { topics, type Topic, type TopicPartial } from "../models";
import { createInsertSchema } from "drizzle-zod";
import path from "node:path";

const schema = createInsertSchema(topics);

// we'll need this later
export async function enrichTopic(sourcePath: string): Promise<Topic> {
  const yamlPath = path.join(sourcePath, "+topic.yml");
  const fields = yaml.load(await Bun.file(yamlPath).text()) as TopicPartial;

  const enriched = { ...fields };
  let changed = false;

  if (!enriched.id) {
    enriched.id = uuidv4();
    changed = true;
  }
  if (!enriched.created_at) {
    enriched.created_at = new Date();
    changed = true;
  }
  if (!enriched.updated_at) {
    enriched.updated_at = new Date();
    changed = true;
  }

  const finalTopic = (await schema.parseAsync(enriched).catch((error) => {
    throw new Error(`Validation failed for ${yamlPath}:\n${error.message}`);
  })) as Topic;

  if (changed) {
    await Bun.write(yamlPath, yaml.dump(finalTopic).trim());
  }

  return finalTopic;
}

export async function hashTopic(sourcePath: string): Promise<[string, string]> {
  const yamlPath = path.join(sourcePath, "+topic.yml");
  const partialTopic = yaml.load(
    await Bun.file(yamlPath).text(),
  ) as TopicPartial;

  const finalTopic = (await schema.parseAsync(partialTopic).catch((error) => {
    throw new Error(`Validation failed for ${yamlPath}:\n${error.message}`);
  })) as Topic;

  const hasher = new Bun.CryptoHasher("sha256");
  hasher.update(JSON.stringify(finalTopic));
  const hash = hasher.digest("hex");

  return [finalTopic.id, hash];
}
