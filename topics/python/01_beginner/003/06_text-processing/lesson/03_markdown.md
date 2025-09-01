### إزالة المسافات: `.strip()`

الـ method المسمى `.strip()` يزيل أي مسافات فارغة (whitespace) من **بداية ونهاية** النص. إنه لا يلمس المسافات في المنتصف.

```python
messy_input = "   Hello, World!   "
clean_input = messy_input.strip()

print(f"النص الأصلي: '{messy_input}'")
print(f"النص النظيف: '{clean_input}'")
```

**الناتج:**

```text
النص الأصلي: '   Hello, World!   '
النص النظيف: 'Hello, World!'
```

لاحظ كيف اختفت المسافات من الحواف فقط.
