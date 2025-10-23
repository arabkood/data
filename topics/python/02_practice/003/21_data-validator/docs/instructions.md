اكتب دالة باسم `validateUser` تأخذ قاموس يمثل مستخدم وتتحقق من صحة البيانات حسب القواعد التالية:
- `name`: يجب أن يكون نص غير فارغ
- `age`: يجب أن يكون رقم بين 18 و 100
- `email`: يجب أن يحتوي على "@" و "."

**المطلوب:**

- الدالة تأخذ معامل واحد: `user` (قاموس)
- الدالة تُرجع قاموس يحتوي على `valid` (True/False) و `errors` (قائمة الأخطاء)
- إذا كانت جميع البيانات صحيحة، أرجع `{"valid": True, "errors": []}`
- إذا كانت هناك أخطاء، أرجع `{"valid": False, "errors": [...]}` مع قائمة الأخطاء

**مثال:**

```python
validateUser({"name": "Ali", "age": 25, "email": "ali@test.com"})
# {"valid": True, "errors": []}

validateUser({"name": "", "age": 25, "email": "ali@test.com"})
# {"valid": False, "errors": ["name is empty"]}

validateUser({"name": "Ali", "age": 15, "email": "ali@test.com"})
# {"valid": False, "errors": ["age must be between 18 and 100"]}

validateUser({"name": "Ali", "age": 25, "email": "invalid"})
# {"valid": False, "errors": ["email must contain @ and ."]}
```
