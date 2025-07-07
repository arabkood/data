import { HuggingFaceTransformersEmbeddings } from "@langchain/community/embeddings/huggingface_transformers";
import { ChatAnthropic } from "@langchain/anthropic";
import { ChatGoogleGenerativeAI } from "@langchain/google-genai";

export const PATHS = {
  documents: "./documents/rag/",
  roadmap: "./documents/roadmap.json",
  styleguide: "./documents/styleguide.md",
};

// export const LLM = () =>
//   new ChatAnthropic({
//     model: "claude-opus-4-20250514",
//     maxTokens: 32000,
//     thinking: {
//       type: "enabled",
//       budget_tokens: 10000
//     },
//     temperature: 1,
//   });

export const LLM = () =>
  new ChatGoogleGenerativeAI({
    model: "gemini-2.5-pro-preview-06-05",
    // model: "gemini-2.5-flash-preview-05-20",
    temperature: 1,
  });

export const EMBEDDINGS = () =>
  new HuggingFaceTransformersEmbeddings({
    model: "Xenova/all-MiniLM-L6-v2",
  });
