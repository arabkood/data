## تطبيق متقدم: تحليل بيانات المبيعات

```python
# بيانات المبيعات: [اسم المنتج، السعر، الكمية المباعة]
products = [
    ["لابتوب", 3000, 5],
    ["هاتف", 1200, 10], 
    ["تابلت", 800, 8],
    ["ساعة ذكية", 500, 15]
]

print("=== تقرير المبيعات ===")
total_revenue = 0
best_selling_product = ""
max_quantity = 0

for product in products:
    name = product[0]
    price = product[1] 
    quantity = product[2]
    revenue = price * quantity
    
    print(f"{name}: {quantity} قطعة × {price} ريال = {revenue} ريال")
    
    total_revenue += revenue
    
    if quantity > max_quantity:
        max_quantity = quantity
        best_selling_product = name

print(f"\nإجمالي الإيرادات: {total_revenue} ريال")
print(f"المنتج الأكثر مبيعاً: {best_selling_product} ({max_quantity} قطعة)")
```

