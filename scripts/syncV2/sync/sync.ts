import { db } from "../db";
import type { CommonTree, DiffTree } from "../diff/diff";
import { createEntities } from "./create";
import { deleteEntities } from "./delete";
import { updateEntities } from "./update";

export async function sync(diffTree: DiffTree, fsPaths: CommonTree) {
  await db.transaction(async (tx) => {
    await deleteEntities(tx, diffTree.toDelete);
    await createEntities(tx, diffTree.toCreate, fsPaths);
    await updateEntities(tx, diffTree.toUpdate, fsPaths);
  });
}
