## الخطأ #4: خطأ المسافة البادئة (Indentation)

**المشكلة:** الكود ليس في المكان الصحيح داخل/خارج الحلقة!

```python
# ⚠️ خطأ: print خارج الحلقة!
for i in range(3):
    total = total + i
print(total)  # سيطبع مرة واحدة فقط
```

**الحل:** ضع الكود في المكان الصحيح!
```python
# ✅ صحيح: لطباعة كل مرة
for i in range(3):
    total = total + i
    print(total)
```

