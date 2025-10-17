**4. KeyError** - مفتاح غير موجود

يحدث عند محاولة الوصول لمفتاح غير موجود في قاموس:

```python
try:
    person = {"name": "أحمد"}
    print(person["age"])  # KeyError!
except KeyError:
    print("المفتاح غير موجود")
```

