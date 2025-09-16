## خطأ النسيان في التحديث

### المشكلة في for:
```python
# نريد تعديل عناصر القائمة
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    num = num * 2  # خطأ: هذا لا يغير القائمة الأصلية!

print(numbers)  # لا تزال [1, 2, 3, 4, 5]
```

### الحل الصحيح:
```python
# استخدام الفهرس لتعديل القائمة
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)  # الآن [2, 4, 6, 8, 10]
```

