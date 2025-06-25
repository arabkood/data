import { dbClient } from "../db";
import { diff } from "../diff/diff";
import { fetchDB } from "../fetcher/fetch";
import { sync } from "../sync/sync";
import { h2 } from "../utils";
import { walk } from "../walker/walk";

async function syncDB() {
  console.log("Connecting to DB...");
  await dbClient.connect();

  h2(
    "PHASE 01: Collected all topics, tracks, modules, and items ids and hashes from the filesystem",
  );
  const { hashes: fsTree, paths: fsTreePaths } = await walk({
    enrich: false,
  });
  console.log(Object.entries(fsTree).map(([k, v]) => [k, v.size]));

  h2("PHASE 02: Fetching ids and hashes from the Database");
  const dbTree = await fetchDB();
  console.log(Object.entries(dbTree).map(([k, v]) => [k, v.size]));

  h2("PHASE 03: Checking diff between db and filesystem");
  const diffTree = await diff(fsTree, dbTree);
  console.log(
    "TO CREATE",
    Object.entries(diffTree.toCreate).map(([k, v]) => [k, v.size]),
  );
  console.log(
    "TO UPDATE",
    Object.entries(diffTree.toUpdate).map(([k, v]) => [k, v.size]),
  );
  console.log(
    "TO DELETE",
    Object.entries(diffTree.toDelete).map(([k, v]) => [k, v.size]),
  );

  h2("PHASE 04: Syncing the DB");

  console.log("Wait and wish for the best....");
  console.log(
    "It either succeeds completely, or it fails completely and leaves the database in the exact state it was in before the operation began, don't worry!",
  );
  await sync(diffTree, fsTreePaths);

  h2("SUCCESS: Data has been synced with the database");
  console.log("Disconnecting from DB...");
  await dbClient.end();
}

await syncDB();
