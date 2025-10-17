**السيناريو 1: نظام الطلاب**

لديك قائمة بطلاب وتريد البحث عن طالب معين:

```python
students = [
    {"id": 1, "name": "أحمد", "gpa": 3.8},
    {"id": 2, "name": "سارة", "gpa": 3.9}
]

# ابحث عن الطالب برقم 2
for student in students:
    if student["id"] == 2:
        print(student["name"])
```

