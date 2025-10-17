# مكتبة معالجة النصوص

## المطلوب

اكتب 4 دوال لمعالجة النصوص.

### الدوال المطلوبة:

1. **reverse_string(text)**: تُرجع النص مقلوباً
   - مثال: `reverse_string("hello")` تُرجع `"olleh"`

2. **count_vowels(text)**: تُرجع عدد الحروف المتحركة (a, e, i, o, u)
   - مثال: `count_vowels("hello")` تُرجع `2`

3. **capitalize_words(text)**: تُرجع النص مع كل كلمة تبدأ بحرف كبير
   - مثال: `capitalize_words("hello world")` تُرجع `"Hello World"`

4. **remove_spaces(text)**: تُرجع النص بدون مسافات
   - مثال: `remove_spaces("hello world")` تُرجع `"helloworld"`

### ثم:
- اختبر كل دالة بطباعة النتيجة

### مثال على المخرجات:

```
olleh
2
Hello World
helloworld
```

### تلميحات:
- للقلب: استخدم `text[::-1]`
- لعد الحروف: استخدم حلقة وتحقق `in "aeiouAEIOU"`
- للحروف الكبيرة: استخدم `.title()`
- لإزالة المسافات: استخدم `.replace(" ", "")`
