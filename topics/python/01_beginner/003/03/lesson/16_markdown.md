يمكنك أيضاً فحص خصائص أخرى مع النوع:

```python
user_age = input("عمرك: ")

if isinstance(user_age, str):
    if user_age.isdigit():  # فحص أن النص يحتوي على أرقام فقط
        print("تم إدخال عمر صحيح!")
    else:
        print("يرجى إدخال أرقام فقط!")
```

هذا يجمع بين فحص النوع وفحص المحتوى!

