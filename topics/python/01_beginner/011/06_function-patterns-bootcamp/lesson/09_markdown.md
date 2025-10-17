**النمط 4: دوال المساعدة**

دوال صغيرة تُستخدم في دوال أكبر:

```python
def _is_weekend(day):  # مساعدة خاصة
    return day in ["السبت", "الأحد"]

def calculate_price(base_price, day):
    if _is_weekend(day):
        return base_price * 1.5
    return base_price
```

