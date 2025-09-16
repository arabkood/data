## خطأ استخدام متغيرات الحلقة خارج نطاقها

### المشكلة:
```python
# في بعض الحالات قد يكون هذا مشكلة
for i in range(3):
    last_number = i

print(f"آخر رقم: {last_number}")  # قد يعمل، لكن ليس أفضل ممارسة
```

### حل أفضل:
```python
last_number = 0  # تعريف واضح خارج الحلقة
for i in range(3):
    last_number = i

print(f"آخر رقم: {last_number}")
```

