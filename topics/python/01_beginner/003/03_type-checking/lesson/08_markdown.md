يمكنك فحص عدة أنواع في نفس الوقت:

```python
value = 42

# فحص نوع واحد
if isinstance(value, int):
    print("رقم صحيح!")

# فحص عدة أنواع
if isinstance(value, (int, float)):
    print("رقم (صحيح أو عشري)!")

# فحص نوع مختلف
if isinstance(value, str):
    print("نص!")
else:
    print("ليس نص!")
```

لاحظ الأقواس `(int, float)` للفحص المتعدد.

