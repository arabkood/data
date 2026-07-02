import { v4 as uuidv4 } from "uuid";
import yaml from "js-yaml";
import path from "node:path";
import { tracks, type Track, type TrackPartial } from "../types";
import { camelCaseKeys, snakeCaseKeys } from "../utils";
import { createInsertSchema } from "drizzle-zod";

const schema = createInsertSchema(tracks);

function extractTrackInfo(trackDir: string): {
	slug: string;
	position: number | null;
} {
	const topicDir = path.dirname(trackDir);
	const trackName = path.basename(trackDir);
	const topicName = path.basename(topicDir);

	if (topicName.includes("@")) {
		throw `Character '@' not allowed in topic name: ${topicDir}`;
	}
	if (trackName.includes("@")) {
		throw `Character '@' not allowed in track name: ${trackDir}`;
	}

	const parseNameAndPosition = (
		name: string,
	): { name: string; position: number | null } => {
		const parts = name.split("_");
		if (parts.length > 1) {
			const position = parseInt(parts[0], 10);
			if (!isNaN(position)) {
				return {
					name: parts.slice(1).join("_"),
					position: position,
				};
			}
		}
		return { name: name, position: 0 };
	};

	const topicInfo = parseNameAndPosition(topicName);
	const trackInfo = parseNameAndPosition(trackName);

	const slug = `${topicInfo.name}-${trackInfo.name}`;

	return {
		slug,
		position: trackInfo.position,
	};
}

// we'll need this later
export async function enrichTrack(
	topicId: string,
	sourcePath: string,
): Promise<Track> {
	const yamlPath = path.join(sourcePath, "+track.yml");
	const rawFields = yaml.load(await Bun.file(yamlPath).text());
	const fields = camelCaseKeys(rawFields) as TrackPartial;

	const enriched = { ...fields };
	let changed = false;

	const { slug, position } = extractTrackInfo(path.dirname(yamlPath));

	if (!enriched.id) {
		enriched.id = uuidv4();
		changed = true;
	}
	if (!enriched.createdAt) {
		enriched.createdAt = new Date();
		changed = true;
	}
	if (enriched.topicId !== topicId) {
		enriched.topicId = topicId;
		changed = true;
	}
	if (enriched.slug !== slug) {
		enriched.slug = slug;
		changed = true;
	}
	if (enriched.position !== position) {
		enriched.position = position;
		changed = true;
	}
	if (!enriched.updatedAt) {
		changed = true;
	}
	if (changed) {
		enriched.updatedAt = new Date();
	}

	const finalTrack = (await schema.parseAsync(enriched).catch((error) => {
		throw new Error(`Validation failed for ${yamlPath}:\n${error.message}`);
	})) as Track;

	if (changed) {
		await Bun.write(yamlPath, yaml.dump(snakeCaseKeys(finalTrack)).trim());
	}

	return finalTrack as Track;
}

export async function hashTrack(sourcePath: string): Promise<[string, string]> {
	const yamlPath = path.join(sourcePath, "+track.yml");
	const rawPartialTrack = yaml.load(await Bun.file(yamlPath).text());
	const partialTrack = camelCaseKeys(rawPartialTrack) as TrackPartial;

	const finalTrack = (await schema.parseAsync(partialTrack).catch((error) => {
		throw new Error(`Validation failed for ${yamlPath}:\n${error.message}`);
	})) as Track;

	const hasher = new Bun.CryptoHasher("sha256");
	hasher.update(JSON.stringify(finalTrack));
	const hash = hasher.digest("hex");

	return [finalTrack.id, hash];
}
