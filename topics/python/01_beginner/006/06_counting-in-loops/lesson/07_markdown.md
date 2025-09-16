## العد الشرطي (Conditional Counting)

أحياناً نريد أن نعد فقط العناصر التي تحقق شرطاً معيناً.

مثال: عد الأرقام الموجبة:

```python
positive_count = 0
numbers = [3, -2, 7, -1, 0, 5]

for num in numbers:
    if num > 0:
        positive_count += 1

print(f"عدد الأرقام الموجبة: {positive_count}")
```

**النتيجة:** `عدد الأرقام الموجبة: 3`

