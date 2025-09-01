### البحث والاستبدال: `.replace()`

أحياناً، تريد استبدال جزء من النص بشيء آخر. الـ method المسمى `.replace()` يقوم بذلك تماماً.

الصيغة هي: `.replace("old", "new")`

```python
sentence = "I love coffee, coffee is the best!"

# استبدل كل "القهوة" بـ "الشاي"
new_sentence = sentence.replace("coffee", "tea")

print(new_sentence)
```

**الناتج:**

```text
I love tea, tea is the best!
```
