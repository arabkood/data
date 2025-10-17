**مهم:** global للتعديل فقط، القراءة لا تحتاجها!

```python
total = 100

def show():
    print(total)  # قراءة - لا تحتاج global ✅

def change():
    global total
    total = 200  # تعديل - تحتاج global ✅
```

