## خطأ الفهرس خارج النطاق (Index Out of Range)

### المشكلة:
```python
# خطأ شائع!
numbers = [10, 20, 30]
for i in range(4):  # خطأ: القائمة بها 3 عناصر فقط!
    print(numbers[i])
```

### رسالة الخطأ:
```
NameError: name 'number' is not defined
```

### الحل:
```python
for i in range(3):
    print(f"الرقم: {i}")  # استخدام i المُعرَّف
```

