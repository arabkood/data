## ⚡ مراجعة التحكم في التدفق

### break - الخروج من الحلقة:
```python
for i in range(10):
    if i == 5:
        break  # توقف عند 5
    print(i)
# النتيجة: 0, 1, 2, 3, 4
```

### continue - تخطي التكرار:
```python
for i in range(5):
    if i == 2:
        continue  # تخطي 2
    print(i)
# النتيجة: 0, 1, 3, 4
```

