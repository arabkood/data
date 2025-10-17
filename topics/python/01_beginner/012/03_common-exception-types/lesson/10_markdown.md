**5. TypeError** - نوع خاطئ

يحدث عند استخدام عملية على نوع خاطئ:

```python
try:
    result = "5" + 10  # TypeError!
except TypeError:
    print("لا يمكن جمع نص ورقم")
```

