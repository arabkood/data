### تجميع النصوص: `.join()`

الـ method المسمى `.join()` هو عكس `.split()`. يأخذ قائمة من النصوص ويجمعها في نص واحد، ويضع "لاصق" (separator) من اختيارك بين كل عنصر.

صيغته غريبة بعض الشيء: `separator.join(list_of_strings)`

```python
words = ["بايثون", "سهل", "وممتع"]

# اجمع الكلمات معاً وضع مسافة بينها
sentence = " ".join(words)
print(sentence)

# اجمع الكلمات معاً وضع "-" بينها
dashed_sentence = "-".join(words)
print(dashed_sentence)
```

**الناتج:**

```text
بايثون سهل وممتع
بايثون-سهل-وممتع
```
