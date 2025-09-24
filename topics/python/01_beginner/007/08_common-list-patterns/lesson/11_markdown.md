## النمط الخامس: الحساب والتجميع 🧮

**المشكلة:** تريد حساب قيمة واحدة من كل القائمة (مجموع، متوسط، أعلى قيمة، إلخ).

**الحل:**
```python
# مثال: حساب المجموع
total = 0

for number in numbers:
    total += number

# مثال: إيجاد الأعلى
highest = numbers[0]  # نبدأ بأول عنصر

for number in numbers:
    if number > highest:
        highest = number
```

