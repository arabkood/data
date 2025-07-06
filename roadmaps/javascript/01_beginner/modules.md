#### **Track: JavaScript for Beginners**

**Module 1: The First Step (الخطوة الأولى)**

- **Goal:** Get the user writing code and seeing immediate output. Build initial confidence.
- **Concepts:**
  1.  `Introduction to JavaScript` (Difficulty: 1, Priority: 5)
  2.  `How to run JavaScript` (Difficulty: 1, Priority: 5)
- **Structure:**
  - **Teach:** A markdown lesson explaining what JS is. A second lesson showing the platform's code runner and `console.log()`.
  - **Practice:** A "fill in the blank" to complete a `console.log("Hello, World!");` statement.
  - **Apply:** A code runner challenge: "Write a program that prints your name and age to the console on separate lines."

**Module 2: Storing Information (تخزين المعلومات)**

- **Goal:** Introduce the fundamental concept of variables and the most common data types.
- **Concepts:**
  1.  `Variables with let and const` (Difficulty: 2, Priority: 5)
  2.  `Data Type: string` (Difficulty: 2, Priority: 5)
  3.  `Data Type: number` (Difficulty: 1, Priority: 5)
  4.  `Variable Naming Rules` (Difficulty: 2, Priority: 4)
- **Structure:**
  - **Teach:** Lessons for each concept. Emphasize the "box" analogy for variables. Show clear examples of `string` vs. `number`.
  - **Practice:** Quizzes on `let` vs. `const`. "Spot the bug" challenges with invalid variable names.
  - **Apply:** Code runner challenge: "Create a `const` for your birth year and a `let` for your current age. Create a `const` for your name. Print them to the console."

**Module 3: Basic Operations (العمليات الأساسية)**

- **Goal:** Teach the user how to manipulate the data they can now store.
- **Concepts:**
  1.  `Arithmetic Operators` (Difficulty: 1, Priority: 5)
  2.  `String Operators (Concatenation)` (Difficulty: 2, Priority: 4)
  3.  `Assignment Operators (=, +=)` (Difficulty: 2, Priority: 5)
- **Structure:**
  - **Teach:** Explain each operator. Crucially, have a lesson dedicated to the `+` operator's dual behavior with numbers vs. strings.
  - **Practice:** "Fill in the blank" exercises for simple math (`2 + 2`) and string concatenation (`"Hello " + "World"`).
  - **Apply:** Code runner challenge: "Create variables `price` and `taxRate`. Calculate the `totalPrice` and store it in a new variable. Then create a string `message` that says 'The total price is: [totalPrice]' and log it."

**Module 4: Making Decisions (اتخاذ القرارات)**

- **Goal:** Introduce the core logic of programming: conditional execution. This is a crucial, high-difficulty module.
- **Concepts:**
  1.  `Data Type: boolean` (Difficulty: 3, Priority: 5)
  2.  `Comparison Operators (===, !==, etc)` (Difficulty: 3, Priority: 5)
  3.  `Logical Operators (&&, ||, !)` (Difficulty: 3, Priority: 5)
  4.  `Control Flow: if...else` (Difficulty: 3, Priority: 5)
- **Structure:**
  - **Teach:** Start with `boolean` as the foundation. Explain that comparisons _produce_ a boolean. Then, show how `if` _consumes_ a boolean to make a decision. Use real-world analogies (e.g., "Is it raining? If `true`, take an umbrella.").
  - **Practice:** "Spot the bug" challenge focusing on the `=` vs `===` pitfall. Quizzes on what `&&` and `||` expressions evaluate to.
  - **Apply:** Code runner challenge: "Write a program that checks if a user's `age` is 18 or over and if they have a `hasLicense` boolean set to `true`. Print different messages based on the outcome."

**Module 5: Handling Lists of Data (التعامل مع قوائم البيانات)**

- **Goal:** Introduce the first major data structure, the Array.
- **Concepts:**
  1.  `Data Structures: Arrays` (Difficulty: 3, Priority: 5)
  2.  `Accessing Array & Object data` (specifically array index access) (Difficulty: 2, Priority: 5)
- **Structure:**
  - **Teach:** Use the analogy of a shopping list or a numbered list of items. Heavily emphasize zero-based indexing. Introduce `.length`, `.push()`, and `.pop()`.
  - **Practice:** "Fill in the blank" to get the first (`[0]`) or last element of an array.
  - **Apply:** Code runner challenge: "Create an array of your favorite movies. Add a new movie to the end. Log the total number of movies and the name of the second movie in the list."

**Module 6: Repeating Actions (تكرار المهام)**

- **Goal:** Combine arrays and loops, a cornerstone of programming. This is another high-difficulty module.
- **Concepts:**
  1.  `Loops: for loop` (Difficulty: 4, Priority: 5)
  2.  `Loops: for...of loop` (Difficulty: 3, Priority: 4) - Taught as the "easier way" for arrays.
- **Structure:**
  - **Teach:** First, teach the classic `for` loop to iterate a set number of times. Then, apply it to an array using `array.length`. Finally, introduce `for...of` as a simpler, more modern syntax for iterating over array _elements_.
  - **Practice:** "Order the code lines" for a standard `for` loop. "Fill in the blank" to complete a `for...of` loop.
  - **Apply:** Code runner challenge: "Given an array of numbers, use a loop to create a new array containing only the numbers greater than 10."

**Module 7: Creating Reusable Code (إنشاء كود قابل لإعادة الاستخدام)**

- **Goal:** Introduce functions to make code organized, reusable, and less repetitive.
- **Concepts:**
  1.  `Functions: Defining and Calling` (Difficulty: 4, Priority: 5)
  2.  `Functions: Parameters & return` (Difficulty: 4, Priority: 5)
  3.  `Functions: Arrow Functions` (Difficulty: 3, Priority: 4)
- **Structure:**
  - **Teach:** Explain the "why" first (Don't Repeat Yourself). Show the syntax for a regular function, then introduce arrow functions as a modern alternative. Spend significant time on `return` vs. `console.log` inside a function.
  - **Practice:** "Spot the bug" where a function is defined but never called. "Fill in the blank" to add parameters to a function definition.
  - **Apply:** Code runner challenge: "Convert the previous module's challenge (filtering numbers from an array) into a reusable function that accepts an array as a parameter and returns the new, filtered array."

**Module 8: The "Aha!" Moment (اللحظة المنتظرة)**

- **Goal:** The payoff. Connect all learned concepts to manipulate a real web page.
- **Concepts:**
  1.  `DOM: Selecting Elements` (Difficulty: 2, Priority: 5)
  2.  `DOM: Changing Content/Styles` (Difficulty: 2, Priority: 5)
  3.  `DOM: Handling Events` (Difficulty: 4, Priority: 5)
- **Structure:**
  - **Teach:** Use simple HTML examples. Explain how JS "sees" the HTML. The most critical part is teaching the event listener callback pattern correctly (passing a function reference, not a function call).
  - **Practice:** Provide HTML and ask the user to write the JS to select a specific element. "Order the code lines" for setting up an event listener.
  - **Apply:** **MINI-PROJECT.** A full "Counter" application. Provide the HTML with a display, an increment button, and a decrement button. The user must write all the JavaScript to select the elements and add click listeners that update the counter value on the page.

**Module 9: A Better Way to Group Data (طريقة أفضل لتنظيم البيانات)**

- **Goal:** Introduce the second major data structure, the Object.
- **Concepts:**
  1.  `Data Structures: Objects` (Difficulty: 3, Priority: 5)
  2.  `Accessing Array & Object data` (specifically dot/bracket notation) (Difficulty: 2, Priority: 5)
- **Structure:**
  - **Teach:** Use the analogy of a "profile" or a dictionary (key-value pairs). Clearly explain the difference between dot and bracket notation.
  - **Practice:** "Fill in the blank" to access a property from a given object.
  - **Apply:** Code runner challenge: "Create a `user` object with properties for `name`, `email`, and `isLoggedIn`. Then, write an `if` statement that checks if the user is logged in and prints a welcome message with their name."

**Module 10: Talking to the Internet (التحدث مع الإنترنت)**

- **Goal:** Introduce the final, most complex topic: asynchronous operations and APIs.
- **Concepts:**
  1.  `Concept of Asynchronicity` (Difficulty: 4, Priority: 4)
  2.  `JSON` (Difficulty: 2, Priority: 4)
  3.  `Promises (.then, .catch)` (Difficulty: 5, Priority: 5)
  4.  `async/await` (Difficulty: 4, Priority: 5) - Taught as the modern, preferred way.
  5.  `Fetch API` (Difficulty: 4, Priority: 5)
- **Structure:**
  - **Teach:** Start with the concept. Use the "ordering food at a restaurant" analogy. Introduce Promises conceptually, but quickly pivot to teaching `async/await` as the practical syntax to use. Cover `try...catch` for error handling here.
  - **Practice:** "Order the code lines" for a full `async` function that uses `fetch`. "Fill in the blank" to correctly `await` a promise and parse the JSON.
  - **Apply:** **MINI-PROJECT.** "Random Cat Fact Generator." Provide HTML with a button and a `p` tag. The user writes an `async` function that `fetches` data from a public API (like `catfact.ninja`) when the button is clicked and displays the fact in the `p` tag.
