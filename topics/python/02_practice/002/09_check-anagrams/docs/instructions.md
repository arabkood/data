اكتب دالة باسم `areAnagrams` تتحقق إذا كانت كلمتين anagrams (أي يحتويان على نفس الحروف بترتيب مختلف).

**المطلوب:**

- الدالة تأخذ معاملين: `word1` و `word2` (نصوص)
- الدالة تُرجع `True` إذا كانت الكلمتان anagrams، وإلا `False`
- تجاهل حالة الأحرف (كبيرة أو صغيرة)
- تجاهل المسافات

**مثال:**

```python
areAnagrams("listen", "silent")      # يُرجع: True
areAnagrams("hello", "world")        # يُرجع: False
areAnagrams("Triangle", "Integral")  # يُرجع: True
areAnagrams("apple", "pale")         # يُرجع: False
```
