**السيناريو 3: كتالوج المنتجات**

تصفية المنتجات حسب السعر:

```python
products = [
    {"name": "قلم", "price": 5, "stock": 100},
    {"name": "كتاب", "price": 50, "stock": 50}
]

# المنتجات أقل من 30 ريال
for product in products:
    if product["price"] < 30:
        print(product["name"])
```

