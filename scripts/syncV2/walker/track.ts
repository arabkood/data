import { v4 as uuidv4 } from "uuid";
import yaml from "js-yaml";
import path from "node:path";
import { tracks, type Track, type TrackPartial } from "../models";
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
	const fields = yaml.load(await Bun.file(yamlPath).text()) as TrackPartial;

	const enriched = { ...fields };
	let changed = false;

	const { slug, position } = extractTrackInfo(path.dirname(yamlPath));

	if (!enriched.id) {
		enriched.id = uuidv4();
		changed = true;
	}
	if (!enriched.created_at) {
		enriched.created_at = new Date();
		changed = true;
	}
	if (enriched.topic_id !== topicId) {
		enriched.topic_id = topicId;
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
	if (!enriched.updated_at) {
		changed = true;
	}
	if (changed) {
		enriched.updated_at = new Date();
	}

	const finalTrack = (await schema.parseAsync(enriched).catch((error) => {
		throw new Error(`Validation failed for ${yamlPath}:\n${error.message}`);
	})) as Track;

	if (changed) {
		await Bun.write(yamlPath, yaml.dump(finalTrack).trim());
	}

	return finalTrack as Track;
}

export async function hashTrack(sourcePath: string): Promise<[string, string]> {
	const yamlPath = path.join(sourcePath, "+track.yml");
	const partialTrack = yaml.load(
		await Bun.file(yamlPath).text(),
	) as TrackPartial;

	const finalTrack = (await schema.parseAsync(partialTrack).catch((error) => {
		throw new Error(`Validation failed for ${yamlPath}:\n${error.message}`);
	})) as Track;

	const hasher = new Bun.CryptoHasher("sha256");
	hasher.update(JSON.stringify(finalTrack));
	const hash = hasher.digest("hex");

	return [finalTrack.id, hash];
}
