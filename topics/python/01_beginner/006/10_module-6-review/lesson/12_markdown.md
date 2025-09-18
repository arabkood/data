## ⏳ مراجعة حلقات While

### البنية الأساسية:
```python
count = 0
while count < 5:
    print(count)
    count += 1  # مهم جداً!
```

### مع المدخلات:
```python
password = ""
while password != "سري":
    password = input("كلمة المرور: ")
print("مرحباً!")
```

### مع break:
```python
while True:
    user_input = input("ادخل 'خروج' للتوقف: ")
    if user_input == "خروج":
        break
    print(f"كتبت: {user_input}")
```

