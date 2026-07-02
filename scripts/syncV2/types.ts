import { type InferSelectModel, type InferInsertModel } from "drizzle-orm";
import { topicsInClass, tracksInClass, modulesInClass, itemsInClass } from "./schema";

export const topics = topicsInClass;
export const tracks = tracksInClass;
export const modules = modulesInClass;
export const items = itemsInClass;


export type Topic = InferSelectModel<typeof topicsInClass>;
export type TopicInsert = InferInsertModel<typeof topicsInClass>;
export type TopicPartial = Partial<TopicInsert>;

export type Track = InferSelectModel<typeof tracksInClass>;
export type TrackInsert = InferInsertModel<typeof tracksInClass>;
export type TrackPartial = Partial<TrackInsert>;

export type Module = InferSelectModel<typeof modulesInClass>;
export type ModuleInsert = InferInsertModel<typeof modulesInClass>;
export type ModulePartial = Partial<ModuleInsert>;

export type Item = InferSelectModel<typeof itemsInClass>;
export type ItemInsert = InferInsertModel<typeof itemsInClass>;
export type ItemPartial = Partial<ItemInsert>;
