اكتب كلاس باسم `RateLimiter` يُحدد عدد الطلبات المسموح بها خلال فترة زمنية.

**المطلوب:**

- الكلاس يأخذ في البناء:
  - `max_requests`: الحد الأقصى للطلبات
  - `time_window`: النافذة الزمنية بالثواني
- يجب تطبيق دالة:
  - `allow_request(user_id, timestamp)`: تُرجع `True` إذا كان الطلب مسموحًا، وإلا `False`
- استخدم Sliding Window لتتبع الطلبات

**مثال:**

```python
limiter = RateLimiter(max_requests=3, time_window=60)
limiter.allow_request("user1", 0)   # True (1st request)
limiter.allow_request("user1", 10)  # True (2nd request)
limiter.allow_request("user1", 20)  # True (3rd request)
limiter.allow_request("user1", 30)  # False (exceeded)
limiter.allow_request("user1", 70)  # True (old requests expired)
```

**ملاحظات:**

- استخدم قاموس يحتفظ بقائمة الطوابع الزمنية لكل مستخدم
- احذف الطلبات القديمة التي خرجت من النافذة الزمنية
- تحقق من عدد الطلبات المتبقية في النافذة
