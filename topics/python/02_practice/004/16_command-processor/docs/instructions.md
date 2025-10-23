اكتب كلاس باسم `CommandProcessor` يُنفذ نظام معالجة أوامر مع دعم التراجع.

**المطلوب:**

- يجب تطبيق الدوال التالية:
  - `register_command(name, execute_fn, undo_fn)`: تُسجل أمرًا جديدًا
  - `execute(name, *args)`: تُنفذ أمرًا وتحفظه في التاريخ
  - `undo()`: تتراجع عن آخر أمر تم تنفيذه
  - `get_history()`: تُرجع قائمة بأسماء الأوامر المنفذة
- كل أمر لديه دالة تنفيذ ودالة تراجع

**مثال:**

```python
processor = CommandProcessor()
state = {"value": 0}

def add_execute(x):
    state["value"] += x

def add_undo(x):
    state["value"] -= x

processor.register_command("add", add_execute, add_undo)
processor.execute("add", 5)    # state["value"] = 5
processor.execute("add", 3)    # state["value"] = 8
processor.undo()               # state["value"] = 5
```

**ملاحظات:**

- احفظ الأوامر المسجلة في قاموس
- احفظ تاريخ الأوامر المنفذة (مع المعاملات)
- عند undo، نفذ دالة undo للأمر الأخير
