اكتب دالة باسم `toHackerSpeak` تأخذ نص وتحوله إلى "لغة الهاكرز" (leetspeak) عبر استبدال بعض الحروف بأرقام ورموز.

**المطلوب:**

- الدالة تأخذ معامل واحد: `text` (نص)
- الدالة تُرجع النص بعد استبدال الحروف حسب القواعد التالية:
 	- a → 4
 	- e → 3
 	- i → 1
 	- o → 0
 	- s → 5
- التحويل يشمل الأحرف الكبيرة والصغيرة
- الحروف الأخرى تبقى كما هي

**مثال:**

```python
toHackerSpeak("hello")          # يُرجع: "h3ll0"
toHackerSpeak("awesome")        # يُرجع: "4w350m3"
toHackerSpeak("HACKER")         # يُرجع: "H4CK3R"
toHackerSpeak("Python is fun")  # يُرجع: "Pyth0n 15 fun"
```
