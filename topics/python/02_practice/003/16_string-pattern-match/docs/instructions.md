اكتب دالة باسم `wordPattern` تأخذ نمط ونص، وتُرجع `True` إذا كان النص يتبع نفس النمط، وإلا `False`.

**المطلوب:**

- الدالة تأخذ معاملين: `pattern` (نمط) و `s` (نص)
- كل حرف في النمط يجب أن يطابق كلمة فريدة في النص
- الكلمات في النص مفصولة بمسافات
- يجب أن تكون المطابقة ثنائية (كل حرف لكلمة واحدة، وكل كلمة لحرف واحد)

**مثال:**

```python
wordPattern("abba", "dog cat cat dog")            # True
wordPattern("abba", "dog cat cat fish")           # False
wordPattern("aaaa", "dog cat cat dog")            # False
wordPattern("abba", "dog dog dog dog")            # False
wordPattern("abc", "dog cat fish")                # True
```
