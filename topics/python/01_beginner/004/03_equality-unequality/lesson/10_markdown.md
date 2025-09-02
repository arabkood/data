**لنجمع كل شيء معًا!**

الآن يمكننا كتابة جمل `if` أكثر ذكاءً. بايثون ستقوم أولاً بتقييم المقارنة، وتحصل على `True` أو `False`، ثم تستخدم هذه النتيجة لتحديد ما إذا كان سيتم تشغيل كتلة الكود أم لا.

```python
password_attempt = "12345"

# الخطوة 1: password_attempt == "password123" تقيّم إلى False
# الخطوة 2: if False: ... لذا يتم تخطي الكتلة
if password_attempt == "password123":
    print("تم تسجيل الدخول بنجاح.")

# الخطوة 1: password_attempt != "password123" تقيّم إلى True
# الخطوة 2: if True: ... لذا يتم تنفيذ الكتلة
if password_attempt != "password123":
    print("كلمة المرور غير صحيحة.")
```

