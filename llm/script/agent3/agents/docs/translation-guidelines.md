## Translation Guidelines

### Tone & Style

- Maintain an **encouraging, friendly, and conversational tone** as if speaking to a peer.
- **Avoid academic formality**—use natural Arabic phrasing (e.g., "لنكتشف معًا!" instead of "سنستكشف").
- **Rephrase, don’t translate literally.** Prioritize clarity over word-for-word accuracy.

---

### Technical Terms

- **First Mention:** **"المصطلح العربي (`English Term`)"** (e.g., **"المُعامِل (`parameter`)"**).
- **Subsequent Mentions:** Use Arabic only (e.g., "`المُعامِل`").

### Code & Content Handling

| **Element**          | **Action**                                                                     | **Example**                    |
| -------------------- | ------------------------------------------------------------------------------ | ------------------------------ |
| **Code Keywords**    | Never translate (`function`, `if`, `console.log`).                             | `function` (✅) / `وظيفة` (❌) |
| **Comments**         | Fully translate Arabic comments.                                               | `// احسب المجموع` (✅)         |
| **User-Facing Text** | Translate strings/UI text.                                                     | `"أدخل اسمك"` (✅)             |
| **Variables/Files**  | Keep variable names in english; add Arabic explanation/comment only if needed. |                                |
| **Analogies**        | Localize concepts.                                                             |                                |

- **Cultural Anchors:**
  - Use Arabic names/contexts
  - Replace culture-specific references (e.g., "هجري" for Hijri calendar).

---

### **Critical Constraints**

- **Emojis:** Use sparingly (max 1 per screen: ✅ → ✨).
- **RULE**: Always surround Technical Terms with `backticks` in any of the languages
- **RULE**: Inside code blocks, **NEVER** mix arabic and english in the same line. If you wanna comment, do it in one language, if you have to mention an english word do it in another line
- **RULE**: Inside code blocks in quizes, when you want to have a placeholder for user input, use this exact characters @@INPUT@@ for placeholders
- Keep the slug same, do not modify it
