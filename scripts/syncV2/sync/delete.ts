import { inArray } from "drizzle-orm";
import type { CommonTree } from "../diff/diff";
import { items, modules, topics, tracks } from "../models";
import type { NodePgTransaction } from "drizzle-orm/node-postgres";

export async function deleteEntities(
  tx: NodePgTransaction<any, any>,
  toDelete: CommonTree,
) {
  const itemIdsToDelete = Array.from(toDelete.items.keys());
  if (itemIdsToDelete.length > 0) {
    await tx.delete(items).where(inArray(items.id, itemIdsToDelete));
  }

  const moduleIdsToDelete = Array.from(toDelete.modules.keys());
  if (moduleIdsToDelete.length > 0) {
    await tx.delete(modules).where(inArray(modules.id, moduleIdsToDelete));
  }

  const trackIdsToDelete = Array.from(toDelete.tracks.keys());
  if (trackIdsToDelete.length > 0) {
    await tx.delete(tracks).where(inArray(tracks.id, trackIdsToDelete));
  }

  const topicIdsToDelete = Array.from(toDelete.topics.keys());
  if (topicIdsToDelete.length > 0) {
    await tx.delete(topics).where(inArray(topics.id, topicIdsToDelete));
  }
}
