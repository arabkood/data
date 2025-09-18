## السيناريو الخامس: نظام حضور الموظفين 👥

في الشركات، نحتاج لتتبع حضور الموظفين وحساب إجمالي ساعات العمل:

```python
total_hours = 0
print("تقرير ساعات العمل الأسبوعية:")

for day in range(1, 8):  # 7 أيام في الأسبوع
    daily_hours = 8  # 8 ساعات يومياً
    print(f"اليوم {day}: {daily_hours} ساعات")
    total_hours += daily_hours  # طريقة مختصرة لـ total_hours = total_hours + daily_hours

print(f"إجمالي ساعات الأسبوع: {total_hours} ساعة")
```

