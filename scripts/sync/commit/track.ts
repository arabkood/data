import { v4 as uuidv4 } from "uuid";
import yaml from "js-yaml";
import path from "node:path";
import { type Track, type TrackPartial } from "../models";
import { change, exists } from "../utils/tracking/checker";

export async function commitTrack(topicId: string, sourcePath: string) {
  try {
    const parentName = path.basename(path.dirname(sourcePath));
    const parentParts = parentName.split("_", 2);
    // const position = parseInt(parentParts[0], 10) || 0;
    const slug = parentParts.length > 1 ? parentParts[1] : parentParts[0];

    // Parse the YAML content
    const yamlData = yaml.load(
      await Bun.file(sourcePath).text(),
    ) as TrackPartial;

    // Separate existing fields into manual and auto
    const manualFields: TrackPartial = {};
    const autoFields: TrackPartial = {};
    Object.entries(yamlData).forEach(([key, value]) => {
      if (
        key === "id" ||
        key === "created_at" ||
        key === "updated_at" ||
        key === "topic_id" ||
        key === "slug"
      ) {
        autoFields[key] = value as any;
      } else {
        // @ts-ignore
        manualFields[key] = value;
      }
    });

    const now = new Date();

    // Set auto fields
    if (!autoFields.id) {
      autoFields.id = uuidv4();
    }
    if (!autoFields.created_at) {
      autoFields.created_at = now;
    }
    // Always update
    autoFields.topic_id = topicId;
    autoFields.slug = slug;

    // 1. Check if file exist under .tracking
    let tracking = await exists<Track>(autoFields.id, "tracks");
    if (tracking) {
      const didChange = !Bun.deepEquals(tracking.data, {
        ...manualFields,
        ...autoFields,
        created_at: autoFields.created_at.toISOString(),
        updated_at: autoFields.updated_at?.toISOString(),
      });
      if (!didChange) {
        // if didn't change don't do nothing, just return
        return {
          ...manualFields,
          ...autoFields,
        } as Track;
      }
    }

    autoFields.updated_at = now;

    // Create the updated YAML content with comments
    const manualContent = yaml.dump(manualFields).trim();
    const autoContent = yaml.dump(autoFields).trim();
    const updatedYamlContent = `${manualContent}\n\n# ----- AUTO-GENERATED FIELDS (DO NOT MODIFY) -----\n${autoContent}`;

    // Write the updated content back to the file
    await Bun.write(sourcePath, updatedYamlContent);

    //2. Write the updated tracking
    await change<Track>(
      autoFields.id,
      "tracks",
      tracking?.status || "changed",
      sourcePath,
      {
        ...manualFields,
        ...autoFields,
      } as Track,
    );

    // Return the combined object
    return {
      ...manualFields,
      ...autoFields,
    } as Track;
  } catch (error) {
    console.error(`Error processing YAML file at ${sourcePath}:`, error);
    throw error;
  }
}
