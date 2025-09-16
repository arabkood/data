## البحث في القوائم

يمكننا البحث عن عنصر معين في القائمة:

```python
fruits = ["تفاح", "موز", "برتقال", "عنب"]
search_fruit = "موز"
found = False

for fruit in fruits:
    if fruit == search_fruit:
        found = True
        break  # توقف عند العثور على العنصر

if found:
    print(f"وُجد {search_fruit} في القائمة!")
else:
    print(f"لم يُوجد {search_fruit} في القائمة")
```

**ملاحظة:** `break` توقف الحلقة فوراً عند العثور على العنصر.

