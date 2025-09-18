## 📋 مراجعة القوائم مع الحلقات

### التكرار المباشر:
```python
colors = ["أحمر", "أزرق", "أخضر"]
for color in colors:
    print(f"اللون: {color}")
```

### مع الفهارس:
```python
for i in range(len(colors)):
    print(f"{i + 1}. {colors[i]}")
```

### إنشاء قائمة جديدة:
```python
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
```

