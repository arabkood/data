import { exists, readdir } from "node:fs/promises";
import type { TrackingStatus, TrackingType } from "./checker";
import { TRACKING_FOLDER, ROOT } from "../../config";
import path, { basename } from "node:path";

export async function cleanupDeleted(type: TrackingType) {
  await Promise.all([
    checkByStatus(type, "changed"),
    checkByStatus(type, "unchanged"),
  ]);
}

async function checkByStatus(type: TrackingType, status: TrackingStatus) {
  const pathToCheck = path.join(TRACKING_FOLDER, type, status);
  const files = await readdir(pathToCheck).catch(() => []);
  for (const file of files) {
    if (file === status) continue;

    const pt = path.resolve(pathToCheck, file);
    const content = await Bun.file(pt).text();
    const expectedPath = path.join(ROOT, content.split("\n")[0]);

    if (!(await exists(expectedPath))) {
      const deletedPath = path.resolve(
        TRACKING_FOLDER,
        type,
        "deleted",
        basename(pt),
      );
      console.log(`${pt} => was moved to deleted`);
      await Bun.write(deletedPath, content);
      await Bun.file(pt).delete();
    }
  }
}
