## الخطأ #3: تعديل القائمة أثناء التكرار

**المشكلة:** تعديل قائمة بينما نمر عليها يسبب سلوكاً غريباً!

```python
# ⚠️ خطير!
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # يعدل القائمة!
```

**الحل:** أنشئ قائمة جديدة أو استخدم نسخة!
```python
# ✅ صحيح
numbers = [1, 2, 3, 4, 5]
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
```

