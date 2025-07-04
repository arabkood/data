لنبدأ ببساطة. هذه دالة تأخذ اسمًا وإجراءً لتنفيذه.

الدالة `performAction` هي **`دالة عالية الرتبة`** لأنها تقبل `sayMarhaba` كوسيط.

```javascript
function sayMarhaba(name) {
  console.log("مرحباً، " + name + "!");
}

function performAction(name, action) {
  // المعامل 'action' هو الآن دالة!
  action(name);
}

// نمرر الدالة sayMarhaba نفسها كأداة
performAction("نور", sayMarhaba);
```

**المُخرجات:**

```
مرحباً، نور!
```

لاحظ أننا مررنا `sayMarhaba` بدون القوسين `()`. نحن نمرر وصفة الدالة، وليس نتيجة تنفيذها.

