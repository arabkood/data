الدوال تعمل معاً كأوركسترا موسيقية! 🎵

دالة تستدعي دالة، التي تستدعي دالة أخرى...

```python
def func_a():
    print("A")
    func_b()

def func_b():
    print("B")
    func_c()

def func_c():
    print("C")

func_a()  # A, B, C
```

