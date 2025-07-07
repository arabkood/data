import { PDFLoader } from "@langchain/community/document_loaders/fs/pdf";
import { TextLoader } from "langchain/document_loaders/fs/text";
import { Chroma } from "@langchain/community/vectorstores/chroma";
import { formatDocumentsAsString } from "langchain/util/document";
import { type Document } from "@langchain/core/documents";
import { EMBEDDINGS, PATHS } from "./config";
import * as fs from "node:fs/promises";
import * as path from "node:path";
import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";

function sanitizeMetadata(documents: Document[]): Document[] {
  return documents.map((doc) => {
    const newMetadata: Record<string, any> = {};
    for (const key in doc.metadata) {
      const value = doc.metadata[key];
      if (
        typeof value === "string" ||
        typeof value === "number" ||
        typeof value === "boolean" ||
        value === null
      ) {
        newMetadata[key] = value;
      } else {
        newMetadata[key] = JSON.stringify(value);
      }
    }
    return { ...doc, metadata: newMetadata };
  });
}

export class RAGService {
  private vectorStore: Chroma | null = null;

  async initialize() {
    if (this.vectorStore) return;

    const EMB = EMBEDDINGS();
    console.log("Initializing RAG service...");

    // Setup vector store
    this.vectorStore = new Chroma(EMB, {
      collectionName: "lesson-docs-agent-1",
      url: "http://localhost:8000",
    });

    await this.indexDocuments();
  }

  private async indexDocuments() {
    if (!this.vectorStore) throw new Error("Vector store not initialized");

    const directoryPath = PATHS.documents;
    const allFiles = await fs.readdir(directoryPath);
    const supportedFiles = allFiles.filter(
      (file) => file.endsWith(".pdf") || file.endsWith(".md"),
    );

    if (supportedFiles.length === 0) {
      console.warn(`No documents found in '${directoryPath}'`);
      return;
    }

    const textSplitter = new RecursiveCharacterTextSplitter({
      chunkSize: 1000,
      chunkOverlap: 200,
    });

    const collection = await this.vectorStore.ensureCollection();
    console.log(`Processing ${supportedFiles.length} documents...`);

    for (let i = 0; i < supportedFiles.length; i++) {
      const file = supportedFiles[i];
      const filePath = path.join(directoryPath, file);
      process.stdout.write(
        `[${i + 1}/${supportedFiles.length}] Checking: ${file}... `,
      );

      const existingDocs = await collection.get({
        where: { source: filePath },
        limit: 1,
      });
      if (existingDocs.ids.length > 0) {
        console.log("Already indexed. Skipping.");
        continue;
      }

      try {
        console.log("New document found. Processing memory-efficiently...");
        let docs: Document[];
        if (file.endsWith(".pdf")) {
          const loader = new PDFLoader(filePath, { splitPages: true });
          docs = await loader.load();
        } else {
          const loader = new TextLoader(filePath);
          docs = await loader.load();
        }

        if (docs.length === 0) {
          console.log(` -> No content found in ${file}, skipping.`);
          continue;
        }

        const batchSize = 50;
        let totalChunksIndexed = 0;
        for (let j = 0; j < docs.length; j += batchSize) {
          const batch = docs.slice(j, j + batchSize);
          const splitDocs = await textSplitter.splitDocuments(batch);
          if (splitDocs.length === 0) continue;
          const sanitizedDocs = sanitizeMetadata(splitDocs);
          await this.vectorStore.addDocuments(sanitizedDocs);
          totalChunksIndexed += sanitizedDocs.length;
          process.stdout.write(
            ` -> Indexed ${totalChunksIndexed} chunks so far...\r`,
          );
        }
        console.log(
          ` -> OK. Finished indexing ${totalChunksIndexed} chunks for ${file}.`,
        );
      } catch (error) {
        console.error(
          `\n[FATAL] Failed to process ${file}. Skipping. Error:`,
          error,
        );
        continue;
      }
    }
  }

  async getInspiration(keywords: string[]): Promise<string> {
    if (!this.vectorStore) {
      throw new Error("RAG service not initialized");
    }

    const searchQuery = keywords.join(" ");

    const retriever = this.vectorStore.asRetriever({
      k: 4,
    });
    const docs = await retriever.invoke(searchQuery);
    const context = formatDocumentsAsString(docs);

    if (!context.trim()) {
      return "No relevant information found in the documents for the given keywords.";
    }

    return `
**Inspiration Material for Keywords: ${keywords.join(", ")}**

**Retrieved Context:**
---
${context}
---

**Key Points to Consider:**
- Extract main theoretical concepts and definitions
- Look for relevant code examples and patterns
- Note best practices and common pitfalls
- Consider practical applications and use cases
`;
  }
}
