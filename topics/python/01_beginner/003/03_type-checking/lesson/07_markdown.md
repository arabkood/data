لنرى `isinstance()` أثناء العمل.

```python
player_name = "LeBron"
player_score = 95

# هل player_name من نوع نص؟
is_string = isinstance(player_name, str)
print(f"هل اسم اللاعب نص؟ {is_string}")

# هل player_score من نوع عدد صحيح؟
is_integer = isinstance(player_score, int)
print(f"هل نقاط اللاعب عدد صحيح؟ {is_integer}")

# هل player_score من نوع نص؟
is_also_string = isinstance(player_score, str)
print(f"هل نقاط اللاعب نص؟ {is_also_string}")
```

**الناتج:**
```text
هل اسم اللاعب نص؟ True
هل نقاط اللاعب عدد صحيح؟ True
هل نقاط اللاعب نص؟ False
```
كما ترى، `isinstance()` هي أداة دقيقة ومباشرة للإجابة على أسئلة "هل هو من نوع...؟".

