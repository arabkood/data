## طرق بديلة للتعامل مع القوائم

### استخدام `enumerate()` للحصول على الفهرس والقيمة معاً:
```python
colors = ["أحمر", "أزرق", "أخضر"]

for index, color in enumerate(colors):
    print(f"{index + 1}. {color}")
```

### استخدام `in` للتحقق من وجود عنصر:
```python
fruits = ["تفاح", "موز", "برتقال"]

if "موز" in fruits:
    print("الموز موجود في القائمة")
```

