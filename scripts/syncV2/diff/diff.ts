import type { DbTree } from "../fetcher/fetch";
import type { FsTree } from "../walker/walk";

export interface CommonTree {
  topics: Map<string, string>;
  tracks: Map<string, string>;
  modules: Map<string, string>;
  items: Map<string, string>;
}

export interface DiffTree {
  toCreate: CommonTree;
  toUpdate: CommonTree;
  toDelete: CommonTree;
}

function diffMaps(
  sourceMap: Map<string, string>,
  dbMap: Map<string, string | null>,
) {
  const toCreate = new Map<string, string>();
  const toUpdate = new Map<string, string>();
  const toDelete = new Map<string, string>();

  for (const [id, sourceHash] of sourceMap.entries()) {
    const dbHash = dbMap.get(id);
    if (dbHash) {
      if (sourceHash !== dbHash) {
        toUpdate.set(id, sourceHash);
      }
    } else {
      toCreate.set(id, sourceHash);
    }
  }

  for (const [id, dbHash] of dbMap.entries()) {
    if (!sourceMap.has(id)) {
      toDelete.set(id, dbHash || "");
    }
  }

  return { toCreate, toUpdate, toDelete };
}

export async function diff(fsTree: FsTree, dbTree: DbTree): Promise<DiffTree> {
  const topicDiff = diffMaps(fsTree.topics, dbTree.topics);
  const trackDiff = diffMaps(fsTree.tracks, dbTree.tracks);
  const moduleDiff = diffMaps(fsTree.modules, dbTree.modules);
  const itemDiff = diffMaps(fsTree.items, dbTree.items);

  return {
    toCreate: {
      topics: topicDiff.toCreate,
      tracks: trackDiff.toCreate,
      modules: moduleDiff.toCreate,
      items: itemDiff.toCreate,
    },
    toUpdate: {
      topics: topicDiff.toUpdate,
      tracks: trackDiff.toUpdate,
      modules: moduleDiff.toUpdate,
      items: itemDiff.toUpdate,
    },
    toDelete: {
      topics: topicDiff.toDelete,
      tracks: trackDiff.toDelete,
      modules: moduleDiff.toDelete,
      items: itemDiff.toDelete,
    },
  };
}
