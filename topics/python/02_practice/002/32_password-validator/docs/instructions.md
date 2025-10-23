اكتب دالة باسم `checkPassword` تتحقق من قوة كلمة المرور حسب القواعد التالية:
- طول 8 أحرف على الأقل
- تحتوي على حرف كبير واحد على الأقل
- تحتوي على حرف صغير واحد على الأقل
- تحتوي على رقم واحد على الأقل

**المطلوب:**

- الدالة تأخذ معامل واحد: `password` (نص)
- الدالة تُرجع `True` إذا استوفت جميع الشروط، وإلا `False`

**مثال:**

```python
checkPassword("Password1")        # يُرجع: True
checkPassword("password")         # يُرجع: False
checkPassword("PASS123")          # يُرجع: False
checkPassword("Pass")             # يُرجع: False
```
