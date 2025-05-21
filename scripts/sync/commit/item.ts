import { v4 as uuidv4 } from "uuid";
import yaml from "js-yaml";
import { type Item, type ItemPartial } from "../models";
import path from "node:path";
import { change, exists } from "../utils/tracking/checker";
import { ROOT } from "../config";

export async function commitItem(moduleId: string, sourcePath: string) {
  try {
    const relativePath = path.relative(
      path.join(ROOT, "topics"),
      path.dirname(sourcePath),
    );
    const parentName = path.basename(path.dirname(sourcePath));
    const parentParts = parentName.split("_", 2);
    const position = parseInt(parentParts[0], 10) || 0;
    const slug = parentParts[1];

    // Parse the YAML content
    const yamlData = yaml.load(
      await Bun.file(sourcePath).text(),
    ) as ItemPartial;

    // Separate existing fields into manual and auto
    const manualFields: ItemPartial = {};
    const autoFields: ItemPartial = {};
    Object.entries(yamlData).forEach(([key, value]) => {
      if (
        key === "id" ||
        key === "created_at" ||
        key === "updated_at" ||
        key === "module_id" ||
        key === "slug" ||
        key === "s3_path" ||
        key === "position"
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
    autoFields.module_id = moduleId;
    autoFields.slug = slug;
    autoFields.position = position;
    autoFields.s3_path = relativePath;

    // 1. Check if file exist under .tracking
    let tracking = await exists<Item>(autoFields.id, "items");
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
        } as Item;
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
    await change<Item>(
      autoFields.id,
      "items",
      tracking?.status || "changed",
      sourcePath,
      {
        ...manualFields,
        ...autoFields,
      } as Item,
    );

    // Return the combined object
    return {
      ...manualFields,
      ...autoFields,
    } as Item;
  } catch (error) {
    console.error(`Error processing YAML file at ${sourcePath}:`, error);
    throw error;
  }
}
