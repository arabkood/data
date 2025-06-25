import { h2 } from "../utils";
import { walk } from "../walker/walk";

async function enrich() {
  h2("TASK: Enriching all topics, tracks, modules, and items with auto fields");
  const { hashes: fsTree, paths: fsTreePaths } = await walk({
    enrich: true,
  });
  console.log(
    "Repo Stats",
    Object.entries(fsTree).map(([k, v]) => [k, v.size]),
  );
  h2("SUCCESS: Content have been enriched");
}

await enrich();
