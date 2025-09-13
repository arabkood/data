### مثال عملي آخر

لنفترض أنك تصمم نظام دخول لمبنى آمن. يُسمح بالدخول إذا كان الشخص:
- موظفاً ولديه بطاقة وصول من المستوى 5.
- **أو** زائراً ومعه مرافق من الموظفين.

يمكننا ترجمة هذه القواعد إلى شرط معقد واحد باستخدام الأقواس لتجميع كل حالة منطقية على حدة.

```python
is_employee = False
keycard_level = 4
is_visitor = True
is_escorted = True

# الحالة الأولى: موظف بمستوى 5
condition1 = (is_employee and keycard_level == 5) # False

# الحالة الثانية: زائر مع مرافق
condition2 = (is_visitor and is_escorted) # True

if condition1 or condition2:
    print("Access Granted.")
else:
    print("Access Denied.")
```
هنا، استخدام الأقواس يجعل المنطق واضحاً جداً: نحن نتحقق من `condition1` أو `condition2`.

