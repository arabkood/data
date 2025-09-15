## أنماط شائعة للحلقات المتداخلة

**1. المربع الكامل (n×n):**
```python
for i in range(n):
    for j in range(n):
        print("■", end="")
    print()
```

**2. المثلث القائم:**
```python
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()
```

**3. التكرار المتعدد الأبعاد:**
```python
for hour in range(24):
    for minute in range(60):
        print(f"{hour:02d}:{minute:02d}")
```

