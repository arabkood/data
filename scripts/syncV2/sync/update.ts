import path from "node:path";
import yaml from "js-yaml";
import { eq } from "drizzle-orm";
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

export async function updateEntities(
  tx: NodePgTransaction<any, any>,
  toUpdate: CommonTree,
  fsPaths: CommonTree,
) {
  const topicUpdatePromises: Promise<any>[] = [];
  toUpdate.topics.forEach((hash, k) => {
    const tPath = fsPaths.topics.get(k);
    if (tPath) {
      topicUpdatePromises.push(
        (async () => {
          const topicData = await getYaml<Topic>(tPath, "+topic.yml", hash);
          return tx.update(topics).set(topicData).where(eq(topics.id, k));
        })(),
      );
    }
  });
  await Promise.all(topicUpdatePromises);

  const trackUpdatePromises: Promise<any>[] = [];
  toUpdate.tracks.forEach((hash, k) => {
    const tPath = fsPaths.tracks.get(k);
    if (tPath) {
      trackUpdatePromises.push(
        (async () => {
          const trackData = await getYaml<Track>(tPath, "+track.yml", hash);
          return tx.update(tracks).set(trackData).where(eq(tracks.id, k));
        })(),
      );
    }
  });
  await Promise.all(trackUpdatePromises);

  const moduleUpdatePromises: Promise<any>[] = [];
  toUpdate.modules.forEach((hash, k) => {
    const mPath = fsPaths.modules.get(k);
    if (mPath) {
      moduleUpdatePromises.push(
        (async () => {
          const moduleData = await getYaml<Module>(mPath, "+module.yml", hash);
          return tx.update(modules).set(moduleData).where(eq(modules.id, k));
        })(),
      );
    }
  });
  await Promise.all(moduleUpdatePromises);

  const itemUpdatePromises: Promise<any>[] = [];
  toUpdate.items.forEach((hash, k) => {
    const iPath = fsPaths.items.get(k);
    if (iPath) {
      itemUpdatePromises.push(
        (async () => {
          const itemData = await getYaml<Item>(iPath, "+item.yml", hash);
          return tx.update(items).set(itemData).where(eq(items.id, k));
        })(),
      );
    }
  });
  await Promise.all(itemUpdatePromises);
}

async function getYaml<T>(
  sourcePath: string,
  name: string,
  hash: string,
): Promise<T> {
  const yamlPath = path.join(sourcePath, name);
  const data = yaml.load(await Bun.file(yamlPath).text()) as any;
  data.hash = hash;
  return data as T;
}
