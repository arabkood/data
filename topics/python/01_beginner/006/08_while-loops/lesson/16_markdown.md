## مثال تطبيقي: آلة حاسبة بسيطة

```python
print("=== آلة حاسبة بسيطة ===")
print("العمليات المتاحة: +, -, *, /")
print("اكتب 'خروج' للإنهاء")

while True:
    operation = input("\nما العملية التي تريد؟ ")
    
    if operation == "خروج":
        print("شكراً لاستخدام الآلة الحاسبة!")
        break
    
    if operation in ["+", "-", "*", "/"]:
        num1 = float(input("الرقم الأول: "))
        num2 = float(input("الرقم الثاني: "))
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/" and num2 != 0:
            result = num1 / num2
        else:
            print("لا يمكن القسمة على صفر!")
            continue
        
        print(f"النتيجة: {num1} {operation} {num2} = {result}")
    else:
        print("عملية غير صحيحة!")
```

