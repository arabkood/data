احذر من هذه الأخطاء الشائعة:

```python
# خطأ شائع - مقارنة مع نص
if type(value) == "int":  # خطأ!
    print("رقم")

# الطريقة الصحيحة
if isinstance(value, int):  # صحيح!
    print("رقم")

# خطأ آخر - نسيان أن input() يعطي str دائماً
age = input("عمرك: ")
if isinstance(age, int):  # هذا دائماً False!
    print("عمر صحيح")
```

