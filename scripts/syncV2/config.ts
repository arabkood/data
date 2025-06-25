import { dirname, resolve } from "node:path";

const __dirname = dirname(import.meta.path);

export const ROOT = resolve(__dirname, "../../");
