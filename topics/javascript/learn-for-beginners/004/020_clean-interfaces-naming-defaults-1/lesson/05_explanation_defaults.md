الآن وبعد أن أصبحت أسماؤنا واضحة، كيف نجعل استدعاء الدوال أسهل؟

> قبل أن نكمل، ما الذي تتوقعه أن يحدث لو استدعينا دالة بمعاملات أقل من المطلوب؟

في كثير من الأحيان، يكون لبعض المعاملات قيمة شائعة. بدلاً من تمريرها في كل مرة، يمكننا تعيين **قيمة افتراضية** باستخدام `=`.

هذا يجعل الـ`:function` أكثر مرونة وأقل عرضة للأخطاء.

```javascript
// بدون قيمة افتراضية
function setPermissions(user, role) {
  // إذا كانت role غير موجودة، ستكون undefined
}

// مع قيمة افتراضية
function setPermissions(user, role = 'guest') {
  console.log(`User: ${user}, Role: ${role}`);
}

setPermissions('Ahmad'); 
// Output: User: Ahmad, Role: guest
```
لاحظ كيف تم استخدام 'guest' تلقائيًا!