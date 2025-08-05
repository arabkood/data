بايثون تقدم طريقة أفضل وأكثر احترافية لفحص الأنواع: الدالة `isinstance()`.

```python
age = 25
name = "سارة"
price = 19.99

print(isinstance(age, int))     # True
print(isinstance(name, str))    # True  
print(isinstance(price, float)) # True
print(isinstance(age, str))     # False
```

`isinstance()` تعطيك `True` إذا كان النوع صحيح، و `False` إذا لم يكن كذلك.

