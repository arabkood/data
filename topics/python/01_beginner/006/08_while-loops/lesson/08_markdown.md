## حلقات while مع العدادات والمجمعات

يمكننا استخدام `while` مع تقنيات العد والتجميع:

```python
total = 0
count = 0
number = 0

print("ادخل أرقاماً (ادخل -1 للتوقف):")
while number != -1:
    number = int(input("الرقم: "))
    if number != -1:
        total += number
        count += 1

if count > 0:
    average = total / count
    print(f"المجموع: {total}")
    print(f"العدد: {count}")
    print(f"المتوسط: {average:.2f}")
```

