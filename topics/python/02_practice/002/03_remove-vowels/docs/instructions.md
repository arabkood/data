اكتب دالة باسم `removeVowels` تأخذ نص وتُرجعه بعد حذف جميع حروف العلة (vowels) منه.

**المطلوب:**

- الدالة تأخذ معامل واحد: `text` (نص)
- الدالة تُرجع النص بعد حذف حروف العلة الإنجليزية: a, e, i, o, u (صغيرة وكبيرة)
- الحروف الأخرى والأرقام والرموز تبقى كما هي

**مثال:**

```python
removeVowels("hello")          # يُرجع: "hll"
removeVowels("world")          # يُرجع: "wrld"
removeVowels("Python")         # يُرجع: "Pythn"
removeVowels("AEIOU")          # يُرجع: ""
removeVowels("xyz123")         # يُرجع: "xyz123"
```
