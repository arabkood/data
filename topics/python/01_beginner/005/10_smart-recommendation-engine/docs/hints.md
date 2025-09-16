#### **بناء الشروط المتداخلة**

```python
if condition:
    # <-- 4 مسافات
    if condition:
        # <-- 8 مسافات
        if condition:
            # <-- 12 مسافات
            pass
        elif condition:
            pass
        else:
            pass
    elif condition:
        pass
    else:
        pass
elif condition:
    pass
else:
    pass
```

#### **الأخطاء الشائعة**

1. نسيان النقطتين `:` بعد `if` و `else`
2. المسافة البادئة غير صحيحة
3. استخدام `=` بدلاً من `==` في المقارنة
4. نسيان تحويل عدد الأشخاص إلى `int`
5. تأكد من كتابة النص بنفس الطريقة: `"sunny"` وليس `"Sunny"`
