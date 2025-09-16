## تتبع القيم الأكبر والأصغر

يمكننا أيضاً تتبع أكبر وأصغر القيم:

```python
numbers = [12, 3, 25, 8, 15]

largest = numbers[0]  # نبدأ بأول عنصر
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"الأكبر: {largest}")
print(f"الأصغر: {smallest}")
```

