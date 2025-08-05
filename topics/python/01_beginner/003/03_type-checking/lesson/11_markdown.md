مثال آخر - التحقق من صحة المدخلات:

```python
name = input("اسمك: ")
age_input = input("عمرك: ")

# التحقق من النوع والمحتوى
if isinstance(name, str) and len(name) > 0:
    print("الاسم صحيح!")
else:
    print("يرجى إدخال اسم صحيح!")

# تذكر: input() دائماً يعطي str
print("نوع المدخل:", type(age_input))
```

هذا يساعدك في بناء برامج أكثر موثوقية.

