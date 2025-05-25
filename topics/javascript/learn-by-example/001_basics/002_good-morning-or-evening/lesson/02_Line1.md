## Line 1: Create a Date Object

We want to tell the computer: "Store the current date in a `variable` called `now`."

```javascript
const now = new Date();
```

This tells the computer to create a new `Date` `object` that holds the current date, time, and time zone. It saves that object in a `constant` named `now`.

You can imagine `now` holding something like:

```yaml
Mon May 25 2025 08:43:00 GMT+0000 (UTC)
```

---

## Quick Breakdown

- `const` => creates a `variable` that won't change
- `now` => the name we give the variable
- `=` => assigns the value
- `new Date()` => built-in time wizard that knows the current time
