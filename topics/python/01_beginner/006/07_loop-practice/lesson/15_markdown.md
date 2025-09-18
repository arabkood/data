## السيناريو السادس: حاسبة الخصومات 💰

المتاجر تقدم خصومات متدرجة حسب كمية الشراء. دعنا ننشئ حاسبة خصومات:

```python
base_price = 100
print("جدول الخصومات:")

for quantity in range(1, 6):
    discount = quantity * 5  # خصم 5% لكل قطعة إضافية
    final_price = base_price - discount
    print(f"عند شراء {quantity} قطع: {final_price} ريال (خصم {discount}%)")
```

