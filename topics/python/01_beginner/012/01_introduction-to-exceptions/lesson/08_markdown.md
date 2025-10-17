**مثال عملي:**

```python
try:
    number = int(input("أدخل رقم: "))
    result = 100 / number
    print(f"النتيجة: {result}")
except:
    print("خطأ! تحقق من إدخالك")

print("البرنامج مستمر!")
```

حتى لو حدث خطأ، البرنامج لا يتوقف!

