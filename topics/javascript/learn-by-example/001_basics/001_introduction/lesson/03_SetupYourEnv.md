## 🚀 Set Up Your Local JavaScript Environment (Fast!)

Want to run JavaScript in your PC? Here’s how to get started with Node.js in just a few minutes.

---

## 1️⃣ Install Node.js

👉 Go to [https://nodejs.org](https://nodejs.org)

- Download the **LTS version** (Long-Term Support)
- Follow the installer steps (click "Next" a few times)

✅ This will install both **Node.js** and **npm** (Node package manager)

---

## 2️⃣ Check Installation

Open your terminal (Command Prompt, Terminal, or PowerShell) and type:

```bash
node -v
```

You should see something like:

```
v22.16.0
```

---

## 3️⃣ Run Your First JavaScript File

1. Create a file named `hello.js`
2. Add this code from last lesson (Don't worry about what this code does for now):

```javascript
const now = new Date();
const hour = now.getHours();

const yourName = "Muhammad";

if (hour < 12) {
  console.log(`Good morning, ${yourName}!`);
} else {
  console.log(`Good evening, ${yourName}!`);
}
```

3. In the terminal, run:

```bash
node hello.js
```

You should see depending on the time of day:

```
Good morning, Muhammad!
```

or

```
Good evening, Muhammad!
```

---

## ✅ You're Ready!

Boom—you just ran JavaScript on your computer! You now have everything you need to start building.
