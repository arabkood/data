## ورشة إصلاح الأخطاء العملية

دعنا نطبق ما تعلمناه على مثال معقد يحتوي على عدة أخطاء:

### الكود الخاطئ:
```python
# برنامج لحساب درجات الطلاب (يحتوي على أخطاء!)
students = ["أحمد", "فاطمة", "سالم"]
grades = [[85, 90], [78, 82, 95], [88]]

for i in range(len(students) + 1):  # خطأ 1
    student_name = students[i]
    student_grades = grades[i]
    
    total = 0
    count = 0
    for grade in student_grades:
        total = grade  # خطأ 2
        count += 1
    
    if count = 0:  # خطأ 3
        average = 0
    else:
        average = total / count
    
    print(f"{student_name}: {average}")
```

