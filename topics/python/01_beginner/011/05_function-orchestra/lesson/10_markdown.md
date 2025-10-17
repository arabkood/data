**دوال مساعدة متداخلة:**

```python
def validate_age(age):
    return age >= 18

def validate_name(name):
    return len(name) > 0

def can_register(name, age):
    if not validate_name(name):
        return False
    if not validate_age(age):
        return False
    return True

print(can_register("أحمد", 25))  # True
```

