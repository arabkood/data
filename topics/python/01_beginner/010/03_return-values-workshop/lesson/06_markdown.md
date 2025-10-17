مهم! `return` تُنهي تنفيذ الدالة فوراً:

```python
def test():
    return 5
    print("لن يُطبع!")  # لن ينفذ أبداً

result = test()  # 5
```

أي كود بعد `return` لن يعمل!

