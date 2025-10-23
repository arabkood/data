اكتب كلاس باسم `CacheWithExpiry` يُخزن البيانات مع وقت انتهاء صلاحية.

**المطلوب:**

- يجب تطبيق الدوال التالية:
  - `set(key, value, ttl, timestamp)`: تُخزن قيمة مع وقت انتهاء (ttl بالثواني)
  - `get(key, timestamp)`: تُرجع القيمة إذا كانت صالحة، وإلا `None`
  - `delete(key)`: تحذف مفتاحًا معينًا
  - `cleanup(timestamp)`: تحذف جميع المفاتيح المنتهية الصلاحية
- إذا انتهت صلاحية المفتاح عند القراءة، احذفه وأرجع `None`

**مثال:**

```python
cache = CacheWithExpiry()
cache.set("key1", "value1", ttl=10, timestamp=0)
cache.get("key1", timestamp=5)   # يُرجع: "value1"
cache.get("key1", timestamp=11)  # يُرجع: None (expired)
```

**ملاحظات:**

- استخدم قاموسين: واحد للقيم وآخر لأوقات الانتهاء
- تحقق من الصلاحية عند كل `get`
- في `cleanup`، احذف جميع المفاتيح المنتهية
