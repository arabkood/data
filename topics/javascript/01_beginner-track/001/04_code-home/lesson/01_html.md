The console is great for quick tests, but for real projects, we need to save our code in files. The standard setup involves two files:

1.  **`index.html`**: The HTML file that structures our webpage.
2.  **`script.js`**: The JavaScript file where we write our code.

How do they connect? We use a special HTML tag, `&lt;script&gt;`, inside our HTML file to tell the browser: "Hey, please load and run the code from this JavaScript file!"

Here is the basic code. Create a folder on your computer, and inside it, create these two files with this exact content.

**File: `index.html`**

```html copy title=index.html
<!DOCTYPE html>
<html>
  <head>
    <title>My First App</title>
  </head>
  <body>
    <h1>Welcome to my website!</h1>

    <!-- This line connects our JavaScript file -->
    <script src="script.js"></script>
  </body>
</html>
```

**File: `script.js`**

```javascript copy title=script.js
console.log("Hello from my file!");
```

Now, if you open the `index.html` file in your browser and check the console, you'll see the message!
