import { eq } from "drizzle-orm";
import { db } from "../db";
import { tracks, type TrackInsert } from "../models";

export async function syncTrack(track: TrackInsert) {
  await db
    .insert(tracks)
    .values(track)
    .onConflictDoUpdate({ target: tracks.id, set: track });
}

export async function deleteTrack(id: string) {
  await db.delete(tracks).where(eq(tracks.id, id));
}
