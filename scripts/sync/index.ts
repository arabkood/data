import { commit } from "./commit/commit";
import { ROOT, TRACKING_FOLDER } from "./config";
import { readdir } from "node:fs/promises";
import { sync } from "./sync2db/sync";
import { init } from "./utils/tracking/checker";
import { cleanupDeleted } from "./utils/tracking/cleanup";
import path from "node:path";

const args = Bun.argv.slice(2);

switch (args[0]) {
  case "commit":
    await init();
    console.log(TRACKING_FOLDER);
    await Promise.all([
      cleanupDeleted("topics"),
      cleanupDeleted("tracks"),
      cleanupDeleted("modules"),
      cleanupDeleted("items"),
    ]);
    const topicsPath = path.resolve(ROOT, "topics");
    const files = await readdir(topicsPath).catch(() => []);
    for (const file of files) {
      const pt = path.resolve(topicsPath, file);
      await commit(pt);
    }
    break;
  case "sync":
    console.log("Syncing...", TRACKING_FOLDER);
    await sync("topics");
    await sync("tracks");
    await sync("modules");
    await sync("items");
    break;
  default:
    console.log("use prepare");
}
