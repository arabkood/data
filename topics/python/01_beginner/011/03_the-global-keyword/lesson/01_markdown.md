كيف نُعدّل متغير عام من داخل دالة؟ 🤔

```python
count = 0

def increment():
    count = count + 1  # خطأ! ❌

increment()
```

Python تظن أن count محلي! نحتاج `global` 🔑

