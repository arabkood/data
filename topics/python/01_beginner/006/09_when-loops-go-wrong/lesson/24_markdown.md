## خطأ الشرط الخاطئ في while

### المشكلة:
```python
# نريد العد من 1 إلى 5
count = 1
while count < 5:  # خطأ: سيتوقف عند 4!
    print(count)
    count += 1
# النتيجة: 1, 2, 3, 4 (بدون 5)
```

### الحل:
```python
count = 1
while count <= 5:  # الحل: <= بدلاً من <
    print(count)
    count += 1
# النتيجة: 1, 2, 3, 4, 5
```

