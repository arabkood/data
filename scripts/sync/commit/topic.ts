import { v4 as uuidv4 } from "uuid";
import yaml from "js-yaml";
import { type Topic, type TopicPartial } from "../models";
import { change, exists } from "../utils/tracking/checker";

export async function commitTopic(sourcePath: string) {
  try {
    // Parse the YAML content
    const yamlData = yaml.load(
      await Bun.file(sourcePath).text(),
    ) as TopicPartial;

    // Separate existing fields into manual and auto
    const manualFields: TopicPartial = {};
    const autoFields: TopicPartial = {};
    Object.entries(yamlData).forEach(([key, value]) => {
      if (key === "id" || key === "created_at" || key === "updated_at") {
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

    // 1. Check if file exist under .tracking
    let tracking = await exists<Topic>(autoFields.id, "topics");
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
        } as Topic;
      }
    }

    // Update the updated_at field
    autoFields.updated_at = now;

    // Create the updated YAML content with comments
    const manualContent = yaml.dump(manualFields).trim();
    const autoContent = yaml.dump(autoFields).trim();
    const updatedYamlContent = `${manualContent}\n\n# ----- AUTO-GENERATED FIELDS (DO NOT MODIFY) -----\n${autoContent}`;

    // Write the updated content back to the file
    await Bun.write(sourcePath, updatedYamlContent);

    //2. Write the updated tracking
    await change<Topic>(
      autoFields.id,
      "topics",
      tracking?.status || "changed",
      sourcePath,
      {
        ...manualFields,
        ...autoFields,
      } as Topic,
    );

    // Return the combined object
    return {
      ...manualFields,
      ...autoFields,
    } as Topic;
  } catch (error) {
    console.error(`Error processing YAML file at ${sourcePath}:`, error);
    throw error;
  }
}
