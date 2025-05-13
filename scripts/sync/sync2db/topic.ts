import { eq } from "drizzle-orm";
import { db } from "../db";
import { topics, type TopicInsert } from "../models";

export async function syncTopic(topic: TopicInsert) {
  await db
    .insert(topics)
    .values(topic)
    .onConflictDoUpdate({ target: topics.id, set: topic });
}

export async function deleteTopic(id: string) {
  await db.delete(topics).where(eq(topics.id, id));
}
