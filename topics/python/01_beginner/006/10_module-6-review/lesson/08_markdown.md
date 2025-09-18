## 🔢 مراجعة العد والتتبع

### عداد بسيط:
```python
count = 0
for i in range(10):
    if i % 2 == 0:  # أرقام زوجية
        count += 1
print(f"عدد الأرقام الزوجية: {count}")
```

### مجمع للقيم:
```python
total = 0
numbers = [5, 10, 15, 20]
for num in numbers:
    total += num
print(f"المجموع: {total}")
```

### متعدد المتغيرات:
```python
positive = 0
negative = 0
for num in [-2, 5, -1, 8, -3]:
    if num > 0:
        positive += 1
    else:
        negative += 1
```

