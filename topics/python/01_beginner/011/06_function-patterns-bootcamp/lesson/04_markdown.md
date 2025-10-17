**النمط 2: دوال المعالجة**

تأخذ بيانات، تعدلها، تُرجعها:

```python
def clean_text(text):
    text = text.strip()
    text = text.lower()
    return text

def format_price(price):
    return f"{price:.2f} ريال"

def normalize_phone(phone):
    return phone.replace("-", "").replace(" ", "")
```

