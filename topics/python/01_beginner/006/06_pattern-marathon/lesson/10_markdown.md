مثلث من **الأرقام** أجمل!

```python
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

الناتج:
```
1
12
123
```

هنا نطبع الرقم `j` بدلاً من النجوم.

