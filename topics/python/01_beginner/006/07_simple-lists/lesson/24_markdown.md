## أفضل الممارسات مع القوائم والحلقات

### ✅ الطرق الصحيحة:
```python
# تكرار مباشر عندما لا نحتاج للفهرس
for item in my_list:
    print(item)

# استخدام enumerate عندما نحتاج للفهرس
for index, item in enumerate(my_list):
    print(f"{index}: {item}")

# استخدام range(len()) عند التعديل على القائمة
for i in range(len(my_list)):
    my_list[i] = my_list[i] * 2
```

### ❌ تجنب هذه الأخطاء:
```python
# خطأ: التكرار على range بدلاً من القائمة
for i in range(my_list):  # خطأ!

# خطأ: فهرس خارج النطاق
for i in range(len(my_list) + 1):  # خطأ!
    print(my_list[i])
```

