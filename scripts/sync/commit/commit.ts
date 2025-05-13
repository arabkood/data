import { readdir, lstat } from "node:fs/promises";
import path from "node:path";
import { commitTrack } from "./track";
import { commitTopic } from "./topic";
import { commitModule } from "./module";
import { commitItem } from "./item";

export async function commit(topicSource: string) {
  const topicPath = path.join(topicSource, "+topic.yml");
  const topic = await commitTopic(topicPath);
  // console.log(`Topic ====> ${topicPath}`);

  const files = await readdir(topicSource);
  const tasks = files.map(async (file) => {
    const fullPath = `${topicSource}/${file}`;
    const stat = await lstat(fullPath);
    if (stat.isDirectory()) {
      await handleTrack(topic.id, fullPath);
    }
  });

  await Promise.all(tasks);
}

async function handleTrack(topicId: string, trackSource: string) {
  const trackPath = path.join(trackSource, "+track.yml");
  const track = await commitTrack(topicId, trackPath);
  // console.log(`Track ====> ${trackPath}`);

  const files = await readdir(trackSource);
  const tasks = files.map(async (file) => {
    const fullPath = `${trackSource}/${file}`;
    const stat = await lstat(fullPath);
    if (stat.isDirectory()) {
      await handleModule(track.id, fullPath);
    }
  });

  await Promise.all(tasks);
}

async function handleModule(trackId: string, moduleSource: string) {
  const modulePath = path.join(moduleSource, "+module.yml");
  const module = await commitModule(trackId, modulePath);
  // console.log(`Module ====> ${modulePath}`);

  const files = await readdir(moduleSource);
  const tasks = files.map(async (file) => {
    const fullPath = `${moduleSource}/${file}`;
    const stat = await lstat(fullPath);
    if (stat.isDirectory()) {
      await handleItem(module.id, fullPath);
    }
  });

  await Promise.all(tasks);
}

async function handleItem(moduleId: string, itemSource: string) {
  const itemPath = path.join(itemSource, "+item.yml");
  const item = await commitItem(moduleId, itemPath);
  // console.log(`Item ====> ${itemPath}`);
}
