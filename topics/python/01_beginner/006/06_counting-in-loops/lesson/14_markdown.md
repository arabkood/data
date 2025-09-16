## تطبيق عملي: محلل النتائج

دعنا نطبق ما تعلمناه في مثال عملي - تحليل درجات الطلاب:

```python
grades = [85, 92, 78, 96, 88, 73, 90]

# متغيرات التتبع
total = 0
count = 0
passed = 0  # درجة النجاح 75 فما فوق
excellent = 0  # درجة ممتاز 90 فما فوق

for grade in grades:
    total += grade
    count += 1
    
    if grade >= 75:
        passed += 1
    if grade >= 90:
        excellent += 1

# النتائج
average = total / count
pass_rate = (passed / count) * 100

print(f"المتوسط: {average:.1f}")
print(f"معدل النجاح: {pass_rate:.1f}%")
print(f"عدد الممتازين: {excellent}")
```

