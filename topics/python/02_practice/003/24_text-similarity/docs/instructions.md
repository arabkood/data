اكتب دالة باسم `textSimilarity` تأخذ نصين وتُرجع نسبة التشابه بينهما بناءً على الكلمات المشتركة.

النسبة = (عدد الكلمات المشتركة × 2) / (مجموع عدد الكلمات في النصين)

**المطلوب:**

- الدالة تأخذ معاملين: `text1` و `text2` (نصان)
- احسب النسبة المئوية للتشابه (0-100)
- تجاهل حالة الأحرف (كبيرة/صغيرة)
- الكلمات مفصولة بمسافات

**مثال:**

```python
textSimilarity("hello world", "hello there")      # 50.0
textSimilarity("hello world", "hello world")      # 100.0
textSimilarity("abc def", "xyz")                  # 0.0
textSimilarity("Hello World", "hello world")      # 100.0
```
