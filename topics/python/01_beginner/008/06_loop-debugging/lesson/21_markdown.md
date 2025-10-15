## الخطأ #8: الحلقات المتداخلة المربكة

**المشكلة:** متغيرات الحلقات المتداخلة لها نفس الاسم!

```python
# ⚠️ مربك!
for i in range(3):
    for i in range(3):  # نفس الاسم!
        print(i)
```

**الحل:** استخدم أسماء مختلفة وواضحة!
```python
# ✅ أفضل
for row in range(3):
    for col in range(3):
        print(f"{row},{col}")
```

