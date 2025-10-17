**1. ValueError** - قيمة غير صحيحة

يحدث عند تحويل قيمة غير مناسبة:

```python
try:
    num = int("abc")  # ValueError!
except ValueError:
    print("لا يمكن تحويل النص لرقم")
```

لاحظ: `except ValueError` تعالج هذا النوع فقط!

