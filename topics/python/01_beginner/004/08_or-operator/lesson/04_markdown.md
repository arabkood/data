### `or` في العمل

لنطبق هذا على مثال عطلة نهاية الأسبوع.

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("استمتع بخصم عطلة نهاية الأسبوع!")
else:
    print("الأسعار العادية تنطبق اليوم.")
```

في هذا المثال، الشرط الأول `day == "Saturday"` هو `False`. لكن الشرط الثاني `day == "Sunday"` هو `True`.
`False or True` يعطي `True`، لذلك يتم تنفيذ كتلة `if` ويحصل المستخدم على الخصم.

