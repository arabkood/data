**السيناريو 2: إحصائيات المبيعات**

حساب إجمالي المبيعات لكل فرع:

```python
sales = {
    "riyadh": [1000, 1500, 1200],
    "jeddah": [900, 1100, 1000]
}

for city, amounts in sales.items():
    total = sum(amounts)
    print(f"{city}: {total}")
```

