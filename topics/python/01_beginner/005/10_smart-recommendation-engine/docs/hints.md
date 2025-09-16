#### **مشكلة المسافات البادئة (Indentation)**

```python
if weather == "rainy":
    activity = "watch movie"    # 4 مسافات
elif weather == "sunny":
    if mood == "energetic":
        if num_people > 1:
            activity = "play football"    # 12 مسافة
```

#### **بناء الشروط المتداخلة**

```python
if weather == "sunny":
    if mood == "energetic":
        if num_people > 1:
            # نشاط للمجموعة
        else:
            # نشاط للفرد
    else:  # mood == "relaxed"
        # نشاط للاسترخاء
```

#### **الأخطاء الشائعة**

1. نسيان النقطتين `:` بعد `if` و `else`
2. عدم محاذاة الكود بشكل صحيح
3. استخدام `=` بدلاً من `==` في المقارنة
4. نسيان تحويل عدد الأشخاص إلى `int`
5. تأكد من كتابة النص بنفس الطريقة: `"sunny"` وليس `"Sunny"`
