import { drizzle } from "drizzle-orm/node-postgres";
import { Client } from "pg";

if (!import.meta.env.DATABASE_URL) {
  throw "First set DATABASE_URL env";
}

console.log(import.meta.env.DATABASE_URL);

export const dbClient = new Client({
  connectionString: import.meta.env.DATABASE_URL,
});

export const db = drizzle({
  client: dbClient,
});
