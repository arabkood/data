## خطأ الخلط بين = و ==

### المشكلة:
```python
password = "سري"
user_input = input("كلمة المرور: ")

if user_input = password:  # خطأ: استخدام = بدلاً من ==
    print("مرحباً")
```

### رسالة الخطأ:
```
SyntaxError: invalid syntax
```

### الحل:
```python
if user_input == password:  # == للمقارنة
    print("مرحباً")
```

**تذكر:**
- `=` للإسناد (وضع قيمة في متغير)
- `==` للمقارنة (هل شيئان متساويان؟)

