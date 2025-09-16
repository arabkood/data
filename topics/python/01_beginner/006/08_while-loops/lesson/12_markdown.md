## while مع الشروط المركبة

يمكننا استخدام عدة شروط مع `and` و `or`:

```python
attempts = 0
max_attempts = 3
correct_password = False

while attempts < max_attempts and not correct_password:
    password = input(f"كلمة المرور (المحاولة {attempts + 1}/{max_attempts}): ")
    attempts += 1
    
    if password == "آمن123":
        correct_password = True
        print("تم تسجيل الدخول بنجاح!")
    else:
        print("كلمة مرور خاطئة")

if not correct_password:
    print("تم تجاوز العدد المسموح من المحاولات")
```

