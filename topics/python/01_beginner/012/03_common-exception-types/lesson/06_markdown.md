**3. IndexError** - فهرس خارج النطاق

يحدث عند محاولة الوصول لفهرس غير موجود:

```python
try:
    items = [1, 2, 3]
    print(items[10])  # IndexError!
except IndexError:
    print("الفهرس غير موجود")
```

