اكتب كلاس باسم `JobScheduler` يُدير جدولة وتنفيذ المهام حسب الأولوية والوقت.

**المطلوب:**

- يجب تطبيق الدوال التالية:
  - `add_job(job_id, priority, execution_time)`: تُضيف مهمة جديدة
  - `get_next_job(current_time)`: تُرجع المهمة التالية المطلوب تنفيذها
  - `remove_job(job_id)`: تحذف مهمة معينة
- المهام تُنفذ حسب:
  1. الوقت (المهام الجاهزة أولًا)
  2. الأولوية الأعلى (رقم أقل = أولوية أعلى)
  3. ترتيب الإضافة (FIFO)

**مثال:**

```python
scheduler = JobScheduler()
scheduler.add_job("job1", priority=2, execution_time=10)
scheduler.add_job("job2", priority=1, execution_time=10)
scheduler.add_job("job3", priority=1, execution_time=5)

scheduler.get_next_job(5)   # "job3"
scheduler.get_next_job(10)  # "job2"
scheduler.get_next_job(10)  # "job1"
```

**ملاحظات:**

- استخدم قائمة أو heap لترتيب المهام
- تحقق من الوقت قبل إرجاع المهمة
- احذف المهمة بعد إرجاعها
