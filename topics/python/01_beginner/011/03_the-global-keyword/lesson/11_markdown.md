**تحذير:** استخدم global بحذر! ⚠️

```python
# ❌ سيء - صعب التتبع
count = 0
def func1():
    global count
    count += 1
def func2():
    global count
    count += 10

# ✅ أفضل - استخدم return
def add_one(n):
    return n + 1
count = add_one(count)
```

استخدم `return` عندما يمكنك!

