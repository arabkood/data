## السيناريو الأخير: تحدي شامل 🎯

الآن دعنا نجمع عدة مفاهيم في تحدي واحد. سنبني برنامج لحساب تكلفة رحلة:

```python
# حساب تكلفة رحلة لعدة أيام
daily_budget = 200
total_cost = 0

print("تقرير مصاريف الرحلة:")
for day in range(1, 8):  # رحلة 7 أيام
    daily_expense = daily_budget + (day * 10)  # المصاريف تزيد مع الوقت
    print(f"اليوم {day}: {daily_expense} ريال")
    total_cost += daily_expense

print(f"إجمالي تكلفة الرحلة: {total_cost} ريال")
average_daily = total_cost / 7
print(f"متوسط المصاريف اليومية: {average_daily} ريال")
```

