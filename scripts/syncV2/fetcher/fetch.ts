import type { PgTableWithColumns } from "drizzle-orm/pg-core";
import { db } from "../db";
import { items, modules, topics, tracks } from "../types";

export interface DbTree {
  topics: Map<string, string | null>;
  tracks: Map<string, string | null>;
  modules: Map<string, string | null>;
  items: Map<string, string | null>;
}

async function fetchMapFor(table: PgTableWithColumns<any>) {
  const result = await db
    .select({
      id: table.id,
      hash: table.hash,
    })
    .from(table);
  return new Map<string, string | null>(result.map((r) => [r.id, r.hash]));
}

/**
 * Main walker function
 */
export async function fetchDB(): Promise<DbTree> {
  const [to, tr, mo, it] = await Promise.all([
    fetchMapFor(topics),
    fetchMapFor(tracks),
    fetchMapFor(modules),
    fetchMapFor(items),
  ]);

  return {
    topics: to,
    tracks: tr,
    modules: mo,
    items: it,
  };
}
