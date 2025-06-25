import { readdir } from "node:fs/promises";
import path, { basename } from "node:path";
import { deleteTopic, syncTopic } from "./topic";
import { deleteItem, syncItem } from "./item";
import { deleteModule, syncModule } from "./module";
import { deleteTrack, syncTrack } from "./track";
import { TRACKING_FOLDER } from "../config";
import type { TrackingType } from "../utils/tracking/checker";
import { db } from "../db";
import { tracks } from "../models";
import { eq } from "drizzle-orm";

export async function sync(type: TrackingType) {
  await syncDeleted(type);
  await syncChanged(type);
}

async function syncChanged(type: TrackingType) {
  const pathToCheck = path.join(TRACKING_FOLDER, type, "changed");
  const files = await readdir(pathToCheck).catch(() => []);
  for (const file of files) {
    if (file === "changed") continue;

    const pt = path.resolve(pathToCheck, file);
    const text = await Bun.file(pt).text();
    const content = JSON.parse(text.split("\n")[1]);
    content.updated_at = new Date(content.updated_at);
    content.created_at = new Date(content.created_at);
    if (type === "topics") {
      await syncTopic(content);
    }
    if (type === "tracks") {
      await syncTrack(content);
    }
    if (type === "modules") {
      await syncModule(content);
    }
    if (type === "items") {
      await syncItem(content);
    }
    const unchangedPath = path.resolve(
      TRACKING_FOLDER,
      type,
      "unchanged",
      basename(pt),
    );
    await Bun.write(unchangedPath, text);
    await Bun.file(pt).delete();
  }
}

async function syncDeleted(type: TrackingType) {
  const pathToCheck = path.join(TRACKING_FOLDER, type, "deleted");
  const files = await readdir(pathToCheck).catch(() => []);
  for (const file of files) {
    if (file === "deleted") continue;

    const pt = path.resolve(pathToCheck, file);
    const id = basename(file);
    if (type === "topics") {
      await deleteTopic(id);
    }
    if (type === "tracks") {
      await deleteTrack(id);
    }
    if (type === "modules") {
      await deleteModule(id);
    }
    if (type === "items") {
      await deleteItem(id);
    }
    await Bun.file(pt).delete();
  }
}
