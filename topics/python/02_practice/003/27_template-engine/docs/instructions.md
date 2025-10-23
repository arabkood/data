اكتب دالة باسم `renderTemplate` تأخذ قالب نصي وقاموس بيانات، وتستبدل المتغيرات في القالب بالقيم من القاموس.

المتغيرات في القالب تكون بالشكل `{{variable_name}}`.

**المطلوب:**

- الدالة تأخذ معاملين: `template` (نص القالب) و `data` (قاموس البيانات)
- الدالة تُرجع النص بعد استبدال جميع المتغيرات
- إذا لم يكن المتغير موجود في البيانات، استبدله بنص فارغ

**مثال:**

```python
renderTemplate("Hello {{name}}!", {"name": "Ali"})
# "Hello Ali!"

renderTemplate("{{x}} + {{y}} = {{z}}", {"x": 1, "y": 2, "z": 3})
# "1 + 2 = 3"

renderTemplate("Hello {{name}}!", {})
# "Hello !"

renderTemplate("No variables", {"x": 1})
# "No variables"
```
