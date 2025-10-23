اكتب كلاس باسم `Graph` يُمثل رسمًا بيانيًا باستخدام قائمة المجاورة (Adjacency List).

**المطلوب:**

- الكلاس يأخذ في البناء `directed` (افتراضيًا `False`)
- يجب تطبيق الدوال التالية:
  - `add_vertex(vertex)`: تُضيف عقدة جديدة
  - `add_edge(v1, v2)`: تُضيف حافة بين عقدتين
  - `get_neighbors(vertex)`: تُرجع قائمة الجيران لعقدة معينة
  - `has_path(start, end)`: تتحقق إذا كان هناك مسار بين عقدتين (استخدم BFS أو DFS)
- إذا كان الرسم غير موجه، الحافة يجب أن تُضاف في الاتجاهين

**مثال:**

```python
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("B", "C")

g.get_neighbors("A")    # يُرجع: ["B"]
g.get_neighbors("B")    # يُرجع: ["A", "C"]
g.has_path("A", "C")    # يُرجع: True
g.has_path("A", "D")    # يُرجع: False
```

**ملاحظات:**

- استخدم قاموس لتخزين العقد وجيرانها
- للبحث عن مسار، استخدم BFS مع طابور أو DFS مع مكدس
