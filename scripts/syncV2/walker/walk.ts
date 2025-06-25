import path from "node:path";
import { ROOT } from "../config";
import yaml from "js-yaml";
import { readdir } from "node:fs/promises";
import { enrichTopic, hashTopic } from "./topic";
import { enrichTrack, hashTrack } from "./track";
import { enrichModule, hashModule } from "./module";
import { enrichItem, hashItem } from "./item";

export interface FsTree {
  topics: Map<string, string>;
  tracks: Map<string, string>;
  modules: Map<string, string>;
  items: Map<string, string>;
}

export interface PathMap {
  topics: Map<string, string>;
  tracks: Map<string, string>;
  modules: Map<string, string>;
  items: Map<string, string>;
}

export interface WalkResult {
  hashes: FsTree;
  paths: PathMap;
}

const CONCURRENCY_LIMITS = {
  topics: 10,
  tracks: 10,
  modules: 10,
  items: 10,
} as const;

async function processWithLimit<T, R>(
  items: T[],
  processor: (item: T) => Promise<R>,
  limit: number,
): Promise<R[]> {
  const results: R[] = [];

  for (let i = 0; i < items.length; i += limit) {
    const batch = items.slice(i, i + limit);
    const batchResults = await Promise.all(batch.map(processor));
    results.push(...batchResults);
  }

  return results;
}

async function getDirectories(dirPath: string): Promise<string[]> {
  try {
    const entries = await readdir(dirPath, { withFileTypes: true });
    return entries
      .filter((entry) => entry.isDirectory())
      .map((entry) => path.resolve(dirPath, entry.name));
  } catch {
    return [];
  }
}

async function processItems(
  modulePaths: string[],
  result: WalkResult,
  opts: WalkOptions,
): Promise<void> {
  const processModule = async (modulePath: string) => {
    const itemPaths = await getDirectories(modulePath);
    const moduleId = await getIdFromYaml(
      path.resolve(modulePath, "+module.yml"),
    );
    if (!moduleId)
      throw `Couldn't get id from ${path.resolve(modulePath, "+module.yml")}`;

    await processWithLimit(
      itemPaths,
      async (itemPath) => {
        if (opts.enrich) {
          await enrichItem(moduleId, itemPath);
        }

        const [id, hash] = await hashItem(itemPath);
        result.hashes.items.set(id, hash);
        result.paths.items.set(id, itemPath);
      },
      CONCURRENCY_LIMITS.items,
    );
  };

  await processWithLimit(
    modulePaths,
    processModule,
    CONCURRENCY_LIMITS.modules,
  );
}

async function processModules(
  trackPaths: string[],
  result: WalkResult,
  opts: WalkOptions,
): Promise<void> {
  const processTrack = async (trackPath: string) => {
    const modulePaths = await getDirectories(trackPath);
    const trackId = await getIdFromYaml(path.resolve(trackPath, "+track.yml"));
    if (!trackId)
      throw `Couldn't get id from ${path.resolve(trackPath, "+track.yml")}`;

    await processWithLimit(
      modulePaths,
      async (modulePath) => {
        if (opts.enrich) {
          await enrichModule(trackId, modulePath);
        }
        const [id, hash] = await hashModule(modulePath);
        result.hashes.modules.set(id, hash);
        result.paths.modules.set(id, modulePath);
      },
      CONCURRENCY_LIMITS.modules,
    );

    await processItems(modulePaths, result, opts);
  };

  await processWithLimit(trackPaths, processTrack, CONCURRENCY_LIMITS.tracks);
}

async function getIdFromYaml(yamlPath: string) {
  const fields = yaml.load(await Bun.file(yamlPath).text()) as { id?: string };
  return fields.id;
}

async function processTracks(
  topicPaths: string[],
  result: WalkResult,
  opts: WalkOptions,
): Promise<void> {
  const processTopic = async (topicPath: string) => {
    const trackPaths = await getDirectories(topicPath);
    const topicId = await getIdFromYaml(path.resolve(topicPath, "+topic.yml"));
    if (!topicId)
      throw `Couldn't get id from ${path.resolve(topicPath, "+topic.yml")}`;

    await processWithLimit(
      trackPaths,
      async (trackPath) => {
        if (opts.enrich) {
          await enrichTrack(topicId, trackPath);
        }
        const [id, hash] = await hashTrack(trackPath);
        result.hashes.tracks.set(id, hash);
        result.paths.tracks.set(id, trackPath);
      },
      CONCURRENCY_LIMITS.tracks,
    );

    await processModules(trackPaths, result, opts);
  };

  await processWithLimit(topicPaths, processTopic, CONCURRENCY_LIMITS.topics);
}

interface WalkOptions {
  enrich?: boolean;
}

async function walk(opts: WalkOptions): Promise<WalkResult> {
  const result: WalkResult = {
    hashes: {
      topics: new Map(),
      tracks: new Map(),
      modules: new Map(),
      items: new Map(),
    },
    paths: {
      topics: new Map(),
      tracks: new Map(),
      modules: new Map(),
      items: new Map(),
    },
  };

  const topicsPath = path.resolve(ROOT, "topics");
  const topicPaths = await getDirectories(topicsPath);

  await processWithLimit(
    topicPaths,
    async (topicPath) => {
      if (opts.enrich) {
        await enrichTopic(topicPath);
      }
      const [id, hash] = await hashTopic(topicPath);
      result.hashes.topics.set(id, hash);
      result.paths.topics.set(id, topicPath);
    },
    CONCURRENCY_LIMITS.topics,
  );

  await processTracks(topicPaths, result, opts);

  return result;
}

export { walk, type FsTree as RepoTree };
