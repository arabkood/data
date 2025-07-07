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
