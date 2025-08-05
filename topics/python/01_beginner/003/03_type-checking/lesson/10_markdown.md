لنرى مثالاً عملياً - برنامج حاسبة بسيط:

```python
def safe_calculate(a, b):
    # فحص أن كلا القيمتين أرقام
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "خطأ: يجب أن تكون القيم أرقام!"

# تجربة
print(safe_calculate(5, 3))      # 8
print(safe_calculate(5, "3"))    # خطأ: يجب أن تكون القيم أرقام!
```

هذا يحمي برنامجك من الأخطاء!

