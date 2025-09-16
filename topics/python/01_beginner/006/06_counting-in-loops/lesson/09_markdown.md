## استخدام عدة متغيرات للتتبع

يمكننا استخدام أكثر من متغير لتتبع معلومات مختلفة في نفس الوقت:

```python
positive_count = 0
negative_count = 0
zero_count = 0

numbers = [3, -2, 0, 7, -1, 0, 5]

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"موجبة: {positive_count}")
print(f"سالبة: {negative_count}")  
print(f"صفر: {zero_count}")
```

