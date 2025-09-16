## استخدام القوائم مع العدادات

يمكننا دمج ما تعلمناه عن العد مع القوائم:

```python
temperatures = [25, 30, 22, 35, 28, 31, 24]
hot_days = 0  # عداد الأيام الحارة (أكثر من 30)

for temp in temperatures:
    print(f"درجة الحرارة: {temp}°C")
    if temp > 30:
        hot_days += 1
        print("يوم حار!")

print(f"عدد الأيام الحارة: {hot_days}")
```

