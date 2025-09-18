## 🧩 تحدي شامل: محلل البيانات

دعنا نطبق كل ما تعلمته في مشروع واحد متكامل:

```python
# بيانات مبيعات لأسبوع
daily_sales = [
    {"day": "السبت", "amount": 1200, "customers": 15},
    {"day": "الأحد", "amount": 1800, "customers": 22}, 
    {"day": "الاثنين", "amount": 950, "customers": 12},
    {"day": "الثلاثاء", "amount": 1600, "customers": 18},
    {"day": "الأربعاء", "amount": 2100, "customers": 28},
    {"day": "الخميس", "amount": 1450, "customers": 17},
    {"day": "الجمعة", "amount": 1900, "customers": 24}
]

# تحليل البيانات
total_sales = 0
total_customers = 0
best_day = ""
best_amount = 0
high_sales_days = 0  # أيام المبيعات العالية (أكثر من 1500)

print("=== تحليل المبيعات الأسبوعية ===")
for day_data in daily_sales:
    day = day_data["day"]
    amount = day_data["amount"]
    customers = day_data["customers"]
    
    # عرض بيانات اليوم
    avg_per_customer = amount / customers
    print(f"{day}: {amount} ريال ({customers} عميل) - متوسط للعميل: {avg_per_customer:.1f}")
    
    # تحديث الإحصائيات
    total_sales += amount
    total_customers += customers
    
    # تحديد أفضل يوم
    if amount > best_amount:
        best_amount = amount
        best_day = day
    
    # عد الأيام عالية المبيعات
    if amount > 1500:
        high_sales_days += 1

# النتائج النهائية
weekly_average = total_sales / len(daily_sales)
customer_average = total_sales / total_customers

print(f"\n=== الملخص ===")
print(f"إجمالي المبيعات: {total_sales} ريال")
print(f"متوسط يومي: {weekly_average:.1f} ريال") 
print(f"إجمالي العملاء: {total_customers}")
print(f"متوسط الإنفاق للعميل: {customer_average:.1f} ريال")
print(f"أفضل يوم: {best_day} ({best_amount} ريال)")
print(f"أيام المبيعات العالية: {high_sales_days} من أصل {len(daily_sales)}")
```

