# تطبيق عملي: البحث في جدول

تخيل أن لديك جدول من الأرقام وتريد البحث عن رقم معين:

```python
# جدول 3×3 من الأرقام
target = 7
found = False

for row in range(3):
    for col in range(3):
        number = row * 3 + col + 1  # ينتج 1,2,3,4,5,6,7,8,9
        print(f"البحث في ({row},{col}): {number}")
        
        if number == target:
            print(f"وجدت الرقم {target} في الموضع ({row},{col})")
            found = True
            break
    
    if found:  # للخروج من الحلقة الخارجية أيضاً
        break

if not found:
    print(f"لم أجد الرقم {target}")
```

