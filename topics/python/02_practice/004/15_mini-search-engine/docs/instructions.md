اكتب كلاس باسم `SearchEngine` يُنشئ فهرسًا للمستندات ويبحث فيها.

**المطلوب:**

- يجب تطبيق الدوال التالية:
  - `add_document(doc_id, text)`: تُضيف مستندًا للفهرس
  - `search(query)`: تبحث عن المستندات التي تحتوي على جميع كلمات الاستعلام
  - `remove_document(doc_id)`: تحذف مستندًا من الفهرس
- البحث يُرجع قائمة بـ doc_ids مرتبة حسب عدد التطابقات
- استخدم Inverted Index (فهرس معكوس)

**مثال:**

```python
engine = SearchEngine()
engine.add_document(1, "Python is a programming language")
engine.add_document(2, "Java is also a programming language")
engine.add_document(3, "Python is popular")

engine.search("Python programming")
# يُرجع: [1, 3] (المستند 1 يحتوي الكلمتين، 3 يحتوي Python فقط)
```

**ملاحظات:**

- احفظ قاموسًا: `word -> set of doc_ids`
- عند البحث، ابحث عن تقاطع المجموعات
- رتب النتائج حسب عدد التطابقات (scoring)
