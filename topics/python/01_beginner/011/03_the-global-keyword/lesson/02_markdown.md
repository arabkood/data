**الكلمة المفتاحية `global`** تخبر Python:

"هذا المتغير عام، ليس محلي!"

```python
count = 0

def increment():
    global count  # الآن Python تعرف!
    count = count + 1  # ✅

increment()
print(count)  # 1
```

