import path from "node:path";
import { ROOT, TRACKING_FOLDER } from "../../config";
import { exists as fsExists, mkdir, stat } from "node:fs/promises";

export type TrackingType = "items" | "modules" | "tracks" | "topics";
export type TrackingStatus = "unchanged" | "changed" | "deleted";

export interface Tracking<T> {
  status: TrackingStatus;
  trackingPath: string;
  path: string;
  data: T;
}

export async function exists<T>(id: string, type: TrackingType) {
  const pathToCheck = path.join(TRACKING_FOLDER, type);

  const found = await Promise.all([
    fsExists(path.join(pathToCheck, "unchanged", id)),
    fsExists(path.join(pathToCheck, "changed", id)),
    fsExists(path.join(pathToCheck, "deleted", id)),
  ]);

  if (!found.includes(true)) {
    return null;
  }
  const status = found[0] ? "unchanged" : found[1] ? "changed" : "deleted";
  const result: Tracking<T> = {
    status: status,
    trackingPath: path.join(pathToCheck, status, id),
    path: "",
    data: {} as T,
  };

  const content = (await Bun.file(result.trackingPath).text()).split("\n", 2);
  result.path = content[0];
  result.data = JSON.parse(content[1]);

  return result;
}

export async function change<T>(
  id: string,
  type: TrackingType,
  oldStatus: TrackingStatus,
  filePath: string,
  data: T,
) {
  const pathToCheck = path.join(TRACKING_FOLDER, type);
  if (oldStatus !== "changed") {
    const trackingPath = path.join(pathToCheck, oldStatus, id);
    await Bun.file(trackingPath).delete();
  }
  const newTrackingPath = path.join(pathToCheck, "changed", id);

  let newContent = path.relative(ROOT, filePath);
  newContent += "\n";
  newContent += JSON.stringify(data);

  await Bun.write(newTrackingPath, newContent);
}

export async function init() {
  try {
    await mkdir(path.join(TRACKING_FOLDER));

    return Promise.all([
      mkdir(path.join(TRACKING_FOLDER, "items")),
      mkdir(path.join(TRACKING_FOLDER, "modules")),
      mkdir(path.join(TRACKING_FOLDER, "tracks")),
      mkdir(path.join(TRACKING_FOLDER, "topics")),
    ]);
  } catch {}
}
