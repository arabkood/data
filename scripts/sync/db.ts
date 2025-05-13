import { drizzle } from "drizzle-orm/node-postgres";

if (!import.meta.env.DATABASE_URL) {
  throw "First set DATABASE_URL env";
}

export const db = drizzle(import.meta.env.DATABASE_URL);
