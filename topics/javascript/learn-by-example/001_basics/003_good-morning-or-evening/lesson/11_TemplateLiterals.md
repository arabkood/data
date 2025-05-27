## Template Literals: Understanding Backticks `\`` and `${}`

Let's look at this code:

```javascript
const yourName = "Muhammad";
console.log(`Good morning, ${yourName}!`);
```

you might notice something new: the `` `backticks` `` and the `${yourName}` part.

### What's a Template Literal?

Using `` `backticks` `` instead of quotes creates what's called a template literal (or template string).

It gives you superpowers like:

- Easily inserting `variables` or `expressions` directly into a string using `${}`
- Write multi-line strings without extra characters or code.

### How It Works

In our example above, JavaScript replaces `${yourName}` with the value stored in the `variable` `yourName`. So behind the scenes, it becomes:

```javascript
console.log(`Good morning, Muhammad!`);
```

### Why Not Use Regular Quotes?

Normally, you'd write it like this:

```javascript
console.log("Good morning, " + yourName + "!");
```

or even like this:

```javascript
console.log("Good morning,", yourName, "!");
```

Both works, but they're not as clean or easy to read when you have multiple variables or longer text.

> Template literals are great! They keep your code tidy and readable, use them when you can!

### Let's Try It Again!

```javascript
const age = 19;
const name = "Muhammad";
const message = `${name} is ${age} years old`;

console.log(message);
```

Output:

```
Muhammad is 19 years old
```
