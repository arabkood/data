import { eq } from "drizzle-orm";
import { db } from "../db";
import { items, type ItemInsert } from "../models";

export async function syncItem(item: ItemInsert) {
  await db
    .insert(items)
    .values(item)
    .onConflictDoUpdate({ target: items.id, set: item });
}

export async function deleteItem(id: string) {
  await db.delete(items).where(eq(items.id, id));
}
