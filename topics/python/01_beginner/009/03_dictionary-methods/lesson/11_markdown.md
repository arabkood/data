يمكن إضافة قيمة افتراضية مع `.get()`:

```python
settings = {"theme": "dark"}

# إن لم يوجد المفتاح، أرجع القيمة الافتراضية
lang = settings.get("language", "ar")
print(lang)  # ar
```

