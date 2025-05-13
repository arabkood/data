import { eq } from "drizzle-orm";
import { db } from "../db";
import { modules, type ModuleInsert } from "../models";

export async function syncModule(module: ModuleInsert) {
  await db
    .insert(modules)
    .values(module)
    .onConflictDoUpdate({ target: modules.id, set: module });
}

export async function deleteModule(id: string) {
  await db.delete(modules).where(eq(modules.id, id));
}
