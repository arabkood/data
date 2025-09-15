# مقارنة بين break و continue

دعني أوضح الفرق بمثال واحد:

```python
print("=== مع break ===")
for i in range(5):
    if i == 3:
        break
    print(i)
    
print("\n=== مع continue ===")
for i in range(5):
    if i == 3:
        continue
    print(i)
```

**النتيجة مع break:** 0, 1, 2 (يتوقف عند 3)
**النتيجة مع continue:** 0, 1, 2, 4 (يتخطى 3 فقط)

