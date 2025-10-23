اكتب دالة باسم `textStats` تأخذ نص وتُرجع قاموس يحتوي على إحصائيات عن النص.

**المطلوب:**

- الدالة تأخذ معامل واحد: `text` (نص)
- الدالة تُرجع قاموس يحتوي على:
  - `chars`: عدد الأحرف (بدون المسافات)
  - `words`: عدد الكلمات
  - `lines`: عدد الأسطر
  - `spaces`: عدد المسافات

**مثال:**

```python
textStats("hello world")
# يُرجع: {"chars": 10, "words": 2, "lines": 1, "spaces": 1}

textStats("hello\nworld")
# يُرجع: {"chars": 10, "words": 2, "lines": 2, "spaces": 0}
```
