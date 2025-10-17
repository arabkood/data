يمكنك تسمية الوسائط عند الاستدعاء:

```python
def info(name, age, city):
    print(f"{name}, {age}, {city}")

# عادي (بالترتيب)
info("أحمد", 25, "جدة")

# بالاسم (أي ترتيب)
info(city="جدة", name="أحمد", age=25)
```

هذا يُسمى **keyword arguments**!

