## التكرار عبر الأرقام في القوائم

يمكننا أيضاً التعامل مع قوائم الأرقام بطريقة مماثلة:

```python
scores = [85, 92, 78, 96, 88]

for score in scores:
    print(f"الدرجة: {score}")
    if score >= 90:
        print("ممتاز!")
    elif score >= 80:
        print("جيد جداً")
    else:
        print("جيد")
```

