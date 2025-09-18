## 🔧 مراجعة إصلاح الأخطاء

### الحلقة اللا نهائية:
```python
# خطأ شائع
i = 0
while i < 5:
    print(i)
    # نسينا i += 1

# الحل
i = 0
while i < 5:
    print(i)
    i += 1  # تحديث المتغير
```

### خطأ الفهرس:
```python
# خطأ
numbers = [1, 2, 3]
for i in range(5):  # خطأ: 5 أكبر من طول القائمة
    print(numbers[i])

# الحل
for i in range(len(numbers)):  # استخدام len()
    print(numbers[i])
```

