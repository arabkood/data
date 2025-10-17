**معالجات متعددة:**

يمكنك استخدام try-except عدة مرات:

```python
try:
    x = int(input("رقم: "))
except:
    print("خطأ 1")

try:
    y = int(input("رقم آخر: "))
except:
    print("خطأ 2")
```

