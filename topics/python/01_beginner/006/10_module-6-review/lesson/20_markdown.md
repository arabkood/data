## 📊 مراجعة الأنماط الشائعة

خلال الوحدة، تعلمت عدة أنماط مهمة تتكرر في البرمجة:

### 1. نمط العد (Counter Pattern):
```python
count = 0
for item in collection:
    if condition:
        count += 1
```

### 2. نمط التجميع (Accumulator Pattern):
```python
total = 0
for number in numbers:
    total += number
```

### 3. نمط البحث (Search Pattern):
```python
found = False
for item in collection:
    if item == target:
        found = True
        break
```

### 4. نمط التحويل (Transform Pattern):
```python
new_list = []
for item in old_list:
    new_item = transform(item)
    new_list.append(new_item)
```

### 5. نمط التحقق (Validation Pattern):
```python
while not is_valid(user_input):
    user_input = input("أعد المحاولة: ")
```

