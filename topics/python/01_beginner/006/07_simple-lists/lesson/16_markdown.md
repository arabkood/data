## تطبيق عملي: إدارة قائمة المهام

دعنا نطبق ما تعلمناه في مثال عملي:

```python
# قائمة المهام مع حالاتها (True = مكتملة، False = غير مكتملة)
tasks = ["دراسة Python", "شراء البقالة", "تنظيف المنزل", "قراءة كتاب"]
completed = [True, False, True, False]

print("=== قائمة المهام ===")
for i in range(len(tasks)):
    status = "✓ مكتمل" if completed[i] else "✗ غير مكتمل"
    print(f"{i + 1}. {tasks[i]} - {status}")

# إحصائيات
total_tasks = len(tasks)
completed_count = 0

for status in completed:
    if status:
        completed_count += 1

remaining = total_tasks - completed_count
print(f"\nالمجموع: {total_tasks}")
print(f"مكتملة: {completed_count}")  
print(f"متبقية: {remaining}")
```

