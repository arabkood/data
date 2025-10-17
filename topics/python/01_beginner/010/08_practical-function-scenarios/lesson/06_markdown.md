**سيناريو 3: الحسابات المالية**

```python
def calculate_vat(amount, rate=15):
    return amount * rate / 100

def total_with_vat(amount, rate=15):
    vat = calculate_vat(amount, rate)
    return amount + vat

price = total_with_vat(100)
print(f"السعر النهائي: {price}")  # 115.0
```

