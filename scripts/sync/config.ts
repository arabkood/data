import { dirname, resolve } from "node:path";

const __dirname = dirname(import.meta.path);

export const TRACKING_FOLDER = resolve(__dirname, "../../", "./.tracking");
export const ROOT = resolve(__dirname, "../../");
