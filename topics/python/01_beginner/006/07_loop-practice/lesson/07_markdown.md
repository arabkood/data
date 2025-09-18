## السيناريو الثالث: حساب فاتورة المطعم 🍽️

تخيل أنك تعمل في مطعم وتحتاج لحساب إجمالي فاتورة الطاولات المختلفة.

```python
total_bill = 0
print("حساب فواتير الطاولات:")

for table in range(1, 4):
    table_bill = table * 25  # كل طاولة لها فاتورة مختلفة
    print(f"الطاولة {table}: {table_bill} ريال")
    total_bill = total_bill + table_bill

print(f"إجمالي اليوم: {total_bill} ريال")
```

