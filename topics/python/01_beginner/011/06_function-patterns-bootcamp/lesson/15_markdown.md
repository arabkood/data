**النمط 6: دوال الحساب**

تحسب وتُرجع نتيجة:

```python
def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"]
    return total

def get_average(numbers):
    return sum(numbers) / len(numbers)
```

