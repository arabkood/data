اكتب دالة باسم `wordFrequency` تأخذ نص وتُرجع قاموس يحتوي على عدد تكرار كل كلمة.

**المطلوب:**

- الدالة تأخذ معامل واحد: `text` (نص)
- الدالة تُرجع قاموس حيث المفتاح هو الكلمة والقيمة هي عدد تكرارها
- تجاهل حالة الأحرف (كبيرة أو صغيرة)

**مثال:**

```python
wordFrequency("hello world hello")        # {"hello": 2, "world": 1}
wordFrequency("Python is fun")            # {"python": 1, "is": 1, "fun": 1}
wordFrequency("test TEST Test")           # {"test": 3}
```
