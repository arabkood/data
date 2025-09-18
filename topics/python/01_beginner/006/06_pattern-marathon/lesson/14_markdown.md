**تحدي الخبراء**: نمط الماس! 💎

```python
# الجزء العلوي
for i in range(1, 4):
    for j in range(3 - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()
```

الناتج:
```
  * 
 * * 
* * * 
```

هذا يستخدم **مسافات فارغة** لإنشاء الشكل!

