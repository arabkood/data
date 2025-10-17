**سيناريو 2: معالجة النصوص**

```python
def clean_text(text):
    text = text.strip()
    text = text.lower()
    return text

def count_words(text):
    cleaned = clean_text(text)
    words = cleaned.split()
    return len(words)

print(count_words("  Hello World  "))  # 2
```

