**سيناريو 4: معالجة القوائم**

```python
def filter_positive(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result

def sum_positive(numbers):
    positive = filter_positive(numbers)
    return sum(positive)
```

