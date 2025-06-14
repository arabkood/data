# ماذا لو حدث خطأ؟ التعامل مع الأخطاء بأناقة

في العالم الحقيقي، قد تفشل طلبات الشبكة (مثل انقطاع الإنترنت أو خطأ في الخادم). استخدام `:async` و `:await` يجعل التعامل مع هذه الأخطاء سهلاً للغاية باستخدام كتلة `:try...catch` المألوفة.

-   ضع الكود الذي قد يفشل (الذي يحتوي على `:await`) داخل كتلة `:try`.
-   التقط أي أخطاء محتملة في كتلة `:catch`.

```javascript
async function safeFetch() {
  try {
    const response = await fetch('https://api.invalid-url.com');
    if (!response.ok) {
      throw new Error('فشل طلب الشبكة');
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("حدث خطأ:", error.message);
  }
}
```

هذا النمط يحافظ على نظافة الكود ويضمن أن تطبيقك يمكنه التعامل مع المشاكل غير المتوقعة.