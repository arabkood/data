# السحر يبدأ مع `async` و `await`

فكر في `:async` و `:await` كطريقة أسهل وأكثر أناقة للتعامل مع كائنات `:Promise`.

1.  **`:async`**: عند وضعها قبل تعريف `:function`، فإنها تجعل الدالة تُرجع `:Promise` دائمًا.
2.  **`:await`**: يمكن استخدامها فقط داخل `:async function`. وظيفتها هي إيقاف تنفيذ الدالة مؤقتًا حتى يتم حل `:Promise`، ثم تستأنف التنفيذ وتُرجع القيمة التي تم حلها.

شاهد كيف تجعل الكود يبدو كأنه متزامن وسهل القراءة:

```javascript
// دالة لجلب بيانات مستخدم
async function fetchUserData() {
  console.log("بدء جلب البيانات...");
  // انتظر هنا حتى تكتمل عملية fetch
  const response = await fetch('https://api.example.com/user/1');
  const data = await response.json(); // انتظر هنا حتى يتم تحليل JSON
  console.log("تم استلام البيانات:", data);
  return data;
}
```

> بإتقانك هذا المفهوم، أصبحت قادراً على كتابة كود غير متزامن يبدو بسيطاً ومنطقياً!