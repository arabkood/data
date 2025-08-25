### التحويل إلى عدد عشري: `float()`

كما رأيت، `int()` صارمة جداً وتقبل الأعداد الصحيحة فقط. ولكن ماذا عن الأسعار، أو درجات الحرارة، أو أي قيمة تحتوي على فاصلة عشرية؟

لهذا نستخدم دالة `float()`. إنها تشبه `int()` ولكنها تحول النص إلى عدد عشري (floating-point number).

```python
price_string = "29.99"
price_number = float(price_string)

print(price_number)
print(type(price_number))
```
**الناتج:**
```text
29.99
<class 'float'>
```

