**سيناريو 1: التحقق من البيانات**

```python
def is_valid_email(email):
    return "@" in email and "." in email

def is_valid_phone(phone):
    return len(phone) == 10 and phone.isdigit()

# استخدام
if is_valid_email("user@example.com"):
    print("بريد صحيح")
```

