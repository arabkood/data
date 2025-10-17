**النمط 3: دوال البناء**

تبني وتُرجع هياكل بيانات:

```python
def create_user(name, age):
    return {
        "name": name,
        "age": age,
        "active": True
    }

def build_message(title, body):
    return f"=== {title} ===\n{body}"
```

