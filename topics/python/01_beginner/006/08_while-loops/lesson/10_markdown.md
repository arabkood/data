## استخدام break و continue مع while

### break - للخروج من الحلقة فوراً:
```python
count = 0
while True:  # حلقة لا نهائية
    count += 1
    print(f"العد: {count}")
    if count >= 3:
        break  # توقف عند 3
print("تم الخروج من الحلقة")
```

### continue - لتخطي باقي التكرار:
```python
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue  # تخطي طباعة 3
    print(f"الرقم: {number}")
```

