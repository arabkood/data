**النمط 1: دوال التحقق**

تُرجع `True` أو `False`:

```python
def is_valid_email(email):
    return "@" in email and "." in email

def is_adult(age):
    return age >= 18

def has_minimum_length(text, min_len=3):
    return len(text) >= min_len
```

