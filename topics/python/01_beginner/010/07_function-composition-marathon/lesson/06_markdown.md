يمكنك بناء سلسلة من الدوال:

```python
def clean(text):
    return text.strip()

def uppercase(text):
    return text.upper()

def add_prefix(text):
    return ">> " + text

# سلسلة
result = add_prefix(uppercase(clean("  hello  ")))
print(result)  # >> HELLO
```

