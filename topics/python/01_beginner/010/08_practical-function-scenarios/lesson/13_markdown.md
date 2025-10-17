**سيناريو 5: تنسيق البيانات**

```python
def format_currency(amount):
    return f"{amount:.2f} ريال"

def format_date(day, month, year):
    return f"{day:02d}/{month:02d}/{year}"

print(format_currency(1234.5))  # 1234.50 ريال
print(format_date(5, 3, 2024))  # 05/03/2024
```

