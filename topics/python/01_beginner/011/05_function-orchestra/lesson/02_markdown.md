**تسلسل الاستدعاء** (Call Stack):

```python
def first():
    print("بداية first")
    second()
    print("نهاية first")

def second():
    print("  بداية second")
    third()
    print("  نهاية second")

def third():
    print("    داخل third")

first()
```

كل دالة تنتهي قبل أن ترجع للتي استدعتها!

