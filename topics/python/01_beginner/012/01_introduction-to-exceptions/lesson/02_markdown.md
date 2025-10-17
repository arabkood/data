**الاستثناءات** (Exceptions) = الأخطاء التي تحدث أثناء التشغيل

عندما يحدث خطأ، Python "ترمي" (throw) استثناء:

```python
# أنواع شائعة من الأخطاء:
int("abc")          # ValueError
10 / 0              # ZeroDivisionError
[1, 2][5]           # IndexError
{"a": 1}["b"]       # KeyError
```

كل خطأ له **نوع** محدد!

