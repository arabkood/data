## النمط الثاني: البحث والإيجاد 🔍

**المشكلة:** تريد معرفة إذا كان عنصر معين موجود في القائمة أو العثور على موقعه.

**الحل:**
```python
# البحث البسيط
if item in my_list:
    print("موجود!")

# إيجاد الموقع
for i, current_item in enumerate(my_list):
    if current_item == target:
        print(f"موجود في الموقع {i}")
        break
```

