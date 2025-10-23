اكتب كلاس باسم `EventSystem` يُنفذ نظام اشتراك ونشر الأحداث (Pub/Sub).

**المطلوب:**

- يجب تطبيق الدوال التالية:
  - `subscribe(event, callback)`: تُسجل دالة للاستماع لحدث معين
  - `unsubscribe(event, callback)`: تُلغي تسجيل دالة من حدث
  - `emit(event, data)`: تُطلق حدثًا وتنفذ جميع الدوال المسجلة
- الـ callback يجب أن يستقبل `data` كمعامل
- يُمكن تسجيل عدة callbacks لنفس الحدث

**مثال:**

```python
events = EventSystem()
results = []

def handler1(data):
    results.append(f"Handler 1: {data}")

def handler2(data):
    results.append(f"Handler 2: {data}")

events.subscribe("message", handler1)
events.subscribe("message", handler2)
events.emit("message", "Hello")
# results: ["Handler 1: Hello", "Handler 2: Hello"]
```

**ملاحظات:**

- استخدم قاموس حيث المفتاح = اسم الحدث، القيمة = قائمة callbacks
- عند emit، نفذ جميع الـ callbacks المسجلة
- تأكد من إمكانية إلغاء التسجيل
