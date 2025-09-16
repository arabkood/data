## أنماط شائعة لحلقات while

### 1. حلقة التحقق من الصحة:
```python
age = -1
while age < 0 or age > 120:
    age = int(input("ادخل عمرك (0-120): "))
    if age < 0 or age > 120:
        print("عمر غير صحيح!")
```

### 2. حلقة القوائم (Menus):
```python
choice = ""
while choice != "خروج":
    print("1. إضافة")
    print("2. حذف") 
    print("3. عرض")
    print("خروج - للخروج")
    choice = input("اختر: ")
```

### 3. حلقة البحث:
```python
numbers = [10, 25, 30, 45, 50]
target = 30
index = 0
found = False

while index < len(numbers) and not found:
    if numbers[index] == target:
        found = True
    else:
        index += 1
```

