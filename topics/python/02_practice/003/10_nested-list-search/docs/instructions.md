اكتب دالة باسم `findInNested` تأخذ قائمة متداخلة وقيمة مستهدفة، وتُرجع `True` إذا وُجدت القيمة في أي مستوى، وإلا `False`.

**المطلوب:**

- الدالة تأخذ معاملين: `nested_list` (قائمة متداخلة) و `target` (القيمة المستهدفة)
- الدالة تبحث في جميع مستويات القائمة
- إذا وُجدت القيمة، أرجع `True`
- إذا لم تُعثر على القيمة، أرجع `False`
- استخدم التكرار الذاتي (recursion)

**مثال:**

```python
findInNested([1, 2, 3], 2)                         # True
findInNested([1, [2, 3], 4], 3)                    # True
findInNested([[1, 2], [3, [4, 5]]], 5)             # True
findInNested([1, 2, 3], 5)                         # False
findInNested([1, [2, [3]]], 4)                     # False
findInNested([], 1)                                # False
```
