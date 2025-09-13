### تقديم المعامل `not`

المعامل `not` هو أبسط معامل منطقي. كل ما يفعله هو **عكس** قيمة `boolean`.

*   `not True` تصبح `False`.
*   `not False` تصبح `True`.

فكر فيه كمفتاح تبديل للضوء. إذا كان الضوء مضاءً (`True`)، فإن `not` يطفئه (`False`). وإذا كان مطفأً (`False`)، فإن `not` يضيئه (`True`).

```python
print(not True)
print(not False)

is_game_over = False
print(not is_game_over)
```

**الناتج:**
```text
False
True
True
```

