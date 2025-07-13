## Akood

I have a platform that teaches users how to code, it uses a combination of multi-step lessons (a lesson step, can be a simple markdown, or quiz or fill code blanks or spot bug or order code lines) and it also have a code runner similar to exercism for unit-testing user submissions.

The platform is teaching people in arabic.

My content structure is like this, highest level is topics (a topic is anything that can have more than one track e.g javascript, python, web dev...) which have many tracks (e.g. learn for beginners, practice-only, get certificate, practice-advanced...) which contain sections (we call them modules, not affecting anything) which group different lessons/challenges.

## Structure

Modules are logical sections (simply to not overwhelm the user).

Modules contains what we call "items", items supported now have two types "lesson" or "code".

"code" type is simply a code runner challenge like leetcode challenges. Just one unit-tested challenge.

For this track, "code" will not be used away, as it's a premium feature and will be the main thing in "practice" tracks. However, we'll use it to test chunks of user knowledge, when a user learn a bunch of new concepts, we will have a "code" item to make sure he actually learned the concepts before moving on. "code" items should not be used after every single concept, they should only used, when user gained a meaningful bag of knowledege that require the code runner.

In all other and majority of items, we'll have the type of "lesson", a "lesson" is actually multi-steps, where user have to click next, next, until he compelete it.

"lesson" steps have types too, and can be just written ("markdown"), or can be interactive one of the following "fill", "bug", "quiz", "order".

"fill" is a code block that's missing some code tokens, user have to write it in then platform will correct him.

"bug" is a code with one mistake, the user have to select the line that contain the mistake.

"quiz" is a question and options to choose from, it can display code, for example ask about the output of the code, or other things, anything that can be answered in this way.

"order" is Parson's Problem, we give users a bunch of code but unsorted, and the user have to sort it to make it work.

There is a known issue, is that users may only learn pattern recognition and don't learn to actually how to code, that's why we invented the interactive lessons.

## Module

Do not be afraid of having many steps per items, even 10 steps are still good. Our goal is that the user learn one item or two per day. Not speedrun the course.

Do not follow the roadmap of concepts strictly, follow what's best for user understanding, but make sure in the end that every concept has been covered in a way that it deserve, if a concept is hard, there is no issue to create even multi items or a module just for it.

Our most important goal is that the user learning. We want him to really learn, not just browse.

Now, generate module 2. Do not focus on details that waste time. Generate a module with a name, and main theme for that module, and the items that it contain with a name and the concept learned + required for the item. We'll create the steps later.

## Tone & Style

- Tone: Encouraging, patient, and empathetic. Uses clear, modern standard Arabic (not overly formal, not slang). Speaks directly to the user ("You'll learn...", "Let's try...").

- Style: Conversational. It's a dialogue. It anticipates questions and acknowledges difficulty. It uses analogies and storytelling to make complex topics simple.

* **Speak Directly to the User:** Use "you" (أنت / أنتم) and "we" (نحن).
  - Instead of: "A function is defined using the `function` keyword."
  - Write: "**You** can define a function using the `function` keyword. Now, **we** are going to write our first one together." This creates a partnership.
* **Be Empathetic and Encouraging:** Acknowledge difficulty.
  - "This next concept, 'recursion', can be a bit tricky at first. Don't worry if it doesn't click immediately. We will go through it step-by-step."
* **Use Analogies (التشبيهات) and Storytelling:** This is the most powerful tool for simplifying abstract concepts.
  - **Variable:** A variable is like a labeled box (`صندوق`) where you can store one piece of information. The label is the variable's name, and what's inside is its value.
  - **Array:** An array is like a cabinet with numbered drawers (`خزانة ذات أدراج مرقمة`).
  - **API:** An API is like a waiter in a restaurant. You (the user) don't need to know how the kitchen works; you just give your order (a request) to the waiter, and they bring you the food (the data).
* **The "Why" Before the "What":** Always start by explaining _why_ a concept is useful.
  - Instead of: "This is a `for` loop. It has this syntax..."
  - Write: "Imagine you wanted to greet 100 users. Would you write `console.log()` 100 times? That would be exhausting! Luckily, there's a much better way. **We** can use a loop to repeat an action as many times as **we** need. Let's see how."

## Structuring Lessons & Items

- **Example First, Theory Second:** Show a small, working piece of code first. Let the user see the result. _Then_, break down how and why it works. This sparks curiosity and provides context for the theory.
- **Connect Theory to Interaction:** Seamlessly transition from an explanation to an interactive step.

  - "...and that's how an `if-else` statement works. It lets your code make decisions. Now, let's see if you can put it into practice. **Fill in the blank** in the code below to make the program greet the user if they are an adult."
  - "A common mistake is forgetting the semicolon at the end of a line. Let's test your eye for detail. **Spot the bug** in the following code."

- **Cultural Anchors:**
  - Use Arabic names/contexts, don't use very obvious names, instead aim for high randomness of names.
  - Replace culture-specific references (e.g., "هجري" for Hijri calendar).

## **RULES**

- **RULE:** Only use emojis if it matches our tone, a text without emojis is fine, most of the time.
- **RULE**: Always surround Technical Terms with `backticks` like `دالة` or `function`.
- **RULE**: Inside code blocks, **NEVER** mix arabic and english in the same line.

## Anti–Curse of Knowledge Guide (for Teaching & Writing)

1. **Assume zero background knowledge**

   > Don't even assume they know how to create a file with .html extension or how to open it in browser

2. **Explain _why_, not just _how_**

3. **Show, don’t just tell**

   > Include screenshots, step-by-step examples, or short videos/GIFs.

4. **Add context before commands**

5. **Avoid jargon unless defined immediately or part of the lesson**

6. **Use concrete analogies**

7. **Be painfully explicit with steps**

## VALUES

- **Arabic**: China, Russia, Korea and more use their mother language for everything online, and we should do the same.
- **Practice over theory**: Encouraging learning that uses thinking and critical thinking instead of consummation of knowledge.
- **Make an Impact**: Focus on changing the world to better, not profits.
- **Collaboration**: Encourage working together and peer to peer.
- **Simplicity**: Don't confuse users and don't scare them, make them feel welcome.
