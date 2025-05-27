## Line 2: Get the Current Hour

Next, we want to tell the computer: "Get the current hour from the `variable` `now` and store it in a variable called `hour`"

```javascript
const hour = now.getHours();
```

Here, the computer use the `.getHours()` method on the `now` object to grab the current hour. It's a part of the built-in `Date` magic wizard.

It returns the current hour as a number from `0` and `23`, and stores that number in a `constant` called `hour`.

So if it's 8:26 AM, you'll get:

```javascript
const hour = 8;
```
