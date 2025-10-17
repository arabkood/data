دوال مساعدة (Helper functions):

```python
def is_valid_age(age):
    return age >= 18 and age <= 100

def can_register(age, has_id):
    return is_valid_age(age) and has_id

print(can_register(25, True))  # True
```

نبني دوال صغيرة ونستخدمها لبناء دوال أكبر!

