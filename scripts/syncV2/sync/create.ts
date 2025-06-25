import path from "node:path";
import yaml from "js-yaml";
import type { CommonTree } from "../diff/diff";
import {
  items,
  modules,
  topics,
  tracks,
  type Item,
  type Module,
  type Topic,
  type Track,
} from "../models";
import type { NodePgTransaction } from "drizzle-orm/node-postgres";

export async function createEntities(
  tx: NodePgTransaction<any, any>,

  toCreate: CommonTree,
  fsPaths: CommonTree,
) {
  const topicsPromises: Promise<Topic>[] = [];
  toCreate.topics.forEach((hash, k) => {
    const tPath = fsPaths.topics.get(k);
    if (tPath) {
      topicsPromises.push(getYaml(tPath, "+topic.yml", hash));
    }
  });
  const topicArr = await Promise.all(topicsPromises);
  if (topicArr.length > 0) {
    await tx.insert(topics).values(topicArr);
  }

  const tracksPromises: Promise<Track>[] = [];
  toCreate.tracks.forEach((hash, k) => {
    const tPath = fsPaths.tracks.get(k);
    if (tPath) {
      tracksPromises.push(getYaml(tPath, "+track.yml", hash));
    }
  });
  const trackArr = await Promise.all(tracksPromises);
  if (trackArr.length > 0) {
    await tx.insert(tracks).values(trackArr);
  }

  const modulesPromises: Promise<Module>[] = [];
  toCreate.modules.forEach((hash, k) => {
    const mPath = fsPaths.modules.get(k);
    if (mPath) {
      modulesPromises.push(getYaml(mPath, "+module.yml", hash));
    }
  });
  const moduleArr = await Promise.all(modulesPromises);
  if (moduleArr.length > 0) {
    await tx.insert(modules).values(moduleArr);
  }

  const itemsPromises: Promise<Item>[] = [];
  toCreate.items.forEach((hash, k) => {
    const iPath = fsPaths.items.get(k);
    if (iPath) {
      itemsPromises.push(getYaml(iPath, "+item.yml", hash));
    }
  });
  const itemArr = await Promise.all(itemsPromises);
  if (itemArr.length > 0) {
    await tx.insert(items).values(itemArr);
  }
}

async function getYaml<T>(
  sourcePath: string,
  name: string,
  hash: string,
): Promise<T> {
  const yamlPath = path.join(sourcePath, name);
  const t = yaml.load(await Bun.file(yamlPath).text()) as any;
  t.hash = hash;
  return t as T;
}
