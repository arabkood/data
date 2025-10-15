يمكنك استخدام `break` و `continue` مع الحلقات المتداخلة!

**تحذير:** `break` يخرج فقط من الحلقة **الداخلية**، وليس الخارجية.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # يخرج من حلقة j فقط
        print(f"i={i}, j={j}")
```

