**إرجاع القيم بين الدوال:**

```python
def get_number():
    return 10

def double_it():
    num = get_number()
    return num * 2

def add_five():
    doubled = double_it()
    return doubled + 5

result = add_five()  # 25
```

