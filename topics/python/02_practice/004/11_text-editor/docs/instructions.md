اكتب كلاس باسم `TextEditor` يُنفذ عمليات أساسية لمحرر نصوص مع دعم Undo/Redo.

**المطلوب:**

- يجب تطبيق الدوال التالية:
  - `write(text)`: تُضيف نص في نهاية المحرر
  - `delete(n)`: تحذف آخر `n` حرف
  - `undo()`: تتراجع عن آخر عملية
  - `redo()`: تُعيد آخر عملية تم التراجع عنها
  - `get_text()`: تُرجع النص الحالي

**مثال:**

```python
editor = TextEditor()
editor.write("hello")
editor.get_text()      # يُرجع: "hello"
editor.write(" world")
editor.get_text()      # يُرجع: "hello world"
editor.delete(6)
editor.get_text()      # يُرجع: "hello"
editor.undo()
editor.get_text()      # يُرجع: "hello world"
editor.redo()
editor.get_text()      # يُرجع: "hello"
```

**ملاحظات:**

- استخدم مكدسين (undo stack و redo stack)
- عند إجراء عملية جديدة، امسح redo stack
- احفظ نسخة من الحالة قبل كل عملية
