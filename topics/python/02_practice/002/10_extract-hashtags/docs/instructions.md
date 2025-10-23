اكتب دالة باسم `extractHashtags` تأخذ نص وتُرجع قائمة بجميع الهاشتاجات الموجودة فيه.

**المطلوب:**

- الدالة تأخذ معامل واحد: `text` (نص)
- الدالة تُرجع قائمة بالهاشتاجات (الكلمات التي تبدأ بـ #)
- الهاشتاج يتكون من # متبوعاً بحروف أو أرقام فقط
- لا تُرجع رمز # في النتيجة

**مثال:**

```python
extractHashtags("I love #python programming")      # ["python"]
extractHashtags("#hello #world")                   # ["hello", "world"]
extractHashtags("No hashtags here")                # []
extractHashtags("#code #test123 #python3")         # ["code", "test123", "python3"]
```
