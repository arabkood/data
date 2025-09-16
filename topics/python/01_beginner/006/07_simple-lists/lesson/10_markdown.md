## إنشاء قوائم جديدة من خلال الحلقات

أحياناً نريد إنشاء قائمة جديدة بناء على قائمة موجودة:

```python
# القائمة الأصلية
prices = [100, 150, 200, 80, 120]

# قائمة جديدة للأسعار مع الخصم 20%
discounted_prices = []

for price in prices:
    new_price = price * 0.8  # خصم 20%
    discounted_prices.append(new_price)

print("الأسعار الأصلية:", prices)
print("الأسعار بعد الخصم:", discounted_prices)
```

**ملاحظة:** `append()` تضيف عنصراً جديداً لنهاية القائمة.

