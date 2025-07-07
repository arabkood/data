## TASK

You are an expert content creator for a fun, interactive coding platform. Your goal is to generate a single micro-lesson that logically follows the previous one.

- Target Audience: {{target}}

### PREVIOUS LEARNED CONCEPTS

{{learned}}

### FULL MODULE CONTEXT

{{module}}

### CURRENT LESSON DETAILS

{{lesson}}

### TASK

You will generate a JSON object containing a files array of distinct, multi-file (steps) lesson variants based on the provided information for the CURRENT lesson.
Crucially, the lesson text MUST connect to the PREVIOUS CONTEXT, creating a smooth transition for the user.
The final output MUST be a single JSON object.

**File Requirements:**

1. Each JSON object from you must be a complete, self-contained lesson
2. Use a mix of .md (markdown) and .yml (quizzes) files
3. Number files sequentially: "01*(lesson_name).md", "02*(quiz_name).yml", etc.
4. Follow ALL rules in the style guide strictly
5. For quizes files, use this structure strictly:
   ```yaml
   type: "quiz"
   lang: "javascript"
   question: |
   code: |
   solution: 0
   options: [...]
   explanation: |
   ```
6. You can use markdown inside quiz file if needed in the following fields: question, options, explanation.
7. Markdown files are not interactive the user can only read the content. For interactions use quizes.
8. In quizes, the explanation field serve only one goal: to explain the user why the solution is the correct solution. Do not use it for other things.

**Metadata Requirements:**
Each lesson variant must also include a `metadata` object with the following fields:

- `title`: A clear, concise title for the lesson
- `blurb`: A short descriptive summary of the lesson
- `difficulty`: One of: `easy`, `medium`, or `hard`
- `base_xp`: An integer representing the XP reward between 100 and 2000
- `type`: Always set to `lesson`
- `slug`: A URL-friendly identifier for the lesson (lowercase, no spaces)

Generate the lesson content now.
