**النطاق** (Scope) = المنطقة التي يمكن استخدام المتغير فيها

هناك نوعان رئيسيان:

1. **Local Scope** (محلي): داخل الدالة فقط
2. **Global Scope** (عام): في كل البرنامج

```python
# Global
name = "أحمد"

def greet():
    # Local
    message = "مرحباً"
    print(name)     # يمكن قراءة العام ✅
    print(message)  # يمكن قراءة المحلي ✅

greet()
print(name)     # ✅
print(message)  # ❌ خطأ! محلي فقط
```

