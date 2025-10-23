اكتب دالة باسم `formatLikes` تأخذ قائمة بأسماء الأشخاص الذين أعجبوا بمنشور، وتُرجع نص منسق حسب عدد الإعجابات.

**القواعد:**

- إذا لم يعجب أحد: `"no one likes this"`
- إذا أعجب شخص واحد: `"{name} likes this"`
- إذا أعجب شخصان: `"{name1} and {name2} like this"`
- إذا أعجب ثلاثة أشخاص: `"{name1}, {name2} and {name3} like this"`
- إذا أعجب 4 أو أكثر: `"{name1}, {name2} and {n} others like this"`

**المطلوب:**

- الدالة تأخذ معامل واحد: `names` (قائمة من النصوص)
- الدالة تُرجع نص منسق حسب القواعد أعلاه

**مثال:**

```python
formatLikes([])                              # "no one likes this"
formatLikes(["Peter"])                       # "Peter likes this"
formatLikes(["Jacob", "Alex"])               # "Jacob and Alex like this"
formatLikes(["Max", "John", "Mark"])         # "Max, John and Mark like this"
formatLikes(["Alex", "Jacob", "Mark", "Max"]) # "Alex, Jacob and 2 others like this"
```
