## الخطأ #6: استخدام break أو continue في المكان الخاطئ

**المشكلة:** break/continue خارج if أو في المكان الخاطئ!

```python
# ⚠️ خطأ: break خارج if
for i in range(10):
    break  # سيتوقف في أول دورة دائماً!
    if i == 5:
        print("وجدنا 5")
```

**الحل:** ضعها في المكان المناسب!
```python
# ✅ صحيح
for i in range(10):
    if i == 5:
        print("وجدنا 5")
        break
```

