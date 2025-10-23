اكتب كلاس باسم `TaskManager` يُدير المهام مع ميزات متقدمة.

**المطلوب:**

- يجب تطبيق الدوال التالية:
  - `add_task(title, priority, tags)`: تُضيف مهمة جديدة
  - `complete_task(task_id)`: تُعلم مهمة كمكتملة
  - `get_tasks(filter_by)`: تُرجع المهام (all/pending/completed)
  - `search_by_tag(tag)`: تُرجع المهام التي تحتوي على وسم معين
  - `get_by_priority(priority)`: تُرجع المهام بأولوية معينة
  - `delete_task(task_id)`: تحذف مهمة
- كل مهمة لها: id، title، priority، tags، status

**مثال:**

```python
tm = TaskManager()
tm.add_task("Buy groceries", priority=1, tags=["shopping", "urgent"])
tm.add_task("Read book", priority=2, tags=["personal"])

tm.get_tasks("pending")        # المهمتين
tm.search_by_tag("urgent")     # "Buy groceries"
tm.complete_task(1)
tm.get_tasks("completed")      # "Buy groceries"
```

**ملاحظات:**

- استخدم قاموس للمهام حيث المفتاح = task_id
- احفظ counter لتوليد IDs فريدة
- المهام يجب أن تُرجع كقوائم أو قواميس
