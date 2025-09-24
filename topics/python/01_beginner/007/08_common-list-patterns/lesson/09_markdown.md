## النمط الرابع: التحويل والتعديل 🔄

**المشكلة:** تريد تطبيق عملية على كل عنصر في القائمة وإنشاء قائمة جديدة بالنتائج.

**الحل:**
```python
# تحويل كل عنصر
transformed_list = []

for item in original_list:
    new_item = transform(item)  # تطبيق التحويل
    transformed_list.append(new_item)
```

مثل تحويل درجات من 100 إلى 10، أو تحويل أسماء إلى أحرف كبيرة.

