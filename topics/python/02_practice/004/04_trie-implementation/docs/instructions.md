اكتب كلاس باسم `Trie` يُنفذ بنية بيانات Trie (شجرة البادئة) لتخزين والبحث عن الكلمات.

**المطلوب:**

- يجب تطبيق الدوال التالية:
  - `insert(word)`: تُضيف كلمة إلى الـ Trie
  - `search(word)`: تُرجع `True` إذا كانت الكلمة موجودة، وإلا `False`
  - `starts_with(prefix)`: تُرجع `True` إذا كان هناك أي كلمة تبدأ بالبادئة المعطاة
- كل عقدة يجب أن تحتفظ بقاموس للحروف التالية
- استخدم علامة لتحديد نهاية الكلمة

**مثال:**

```python
trie = Trie()
trie.insert("apple")
trie.search("apple")       # يُرجع: True
trie.search("app")         # يُرجع: False
trie.starts_with("app")    # يُرجع: True
trie.insert("app")
trie.search("app")         # يُرجع: True
```

**ملاحظات:**

- استخدم كلاس `TrieNode` لتمثيل كل عقدة
- كل عقدة تحتوي على قاموس للأطفال وعلامة `is_end_of_word`
