## خطأ المنطق في الحلقات المتداخلة

### المشكلة:
```python
# نريد طباعة جدول الضرب لكن هناك خطأ منطقي
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i + j}")  # خطأ: + بدلاً من *
```

### الحل:
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")  # الآن صحيح
```

