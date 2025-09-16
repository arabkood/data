## أخطاء شائعة في حلقات while

### 1. شرط البداية خاطئ:
```python
# خطأ: الشرط خاطئ من البداية
count = 10
while count < 5:  # لن تعمل أبداً!
    print(count)
    count += 1
```

### 2. تحديث خاطئ:
```python
# خطأ: تحديث في الاتجاه الخاطئ
count = 0
while count < 5:
    print(count)
    count -= 1  # خطأ: ينقص بدلاً من أن يزيد!
```

### 3. نسيان حالات الخروج:
```python
# خطأ: لا توجد طريقة للخروج
while True:
    user_input = input("ادخل 'خروج' للتوقف: ")
    if user_input == "خروج":
        print("وداعاً")
        # نسينا break!
```

