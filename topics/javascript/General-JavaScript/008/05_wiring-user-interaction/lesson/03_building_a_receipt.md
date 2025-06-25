عمل رائع! يمكن لبرنامجنا الآن إنشاء رسائل مخصصة. هذه أداة قوية.

لنطبّق هذا على سيناريو واقعي. ليلى تدير متجرًا صغيرًا للبهارات عبر الإنترنت وتحتاج إلى إنشاء رسالة لعملائها.

---

يمكننا بناء سلسلة نصية أكثر تعقيدًا قبل طباعتها. هذا يحافظ على الشيفرة نظيفة وسهلة القراءة.

**ركّز على كيفية إنشاء `message`** قبل استخدام `console.log`.

```javascript
function createReceipt(itemName, price, quantity) {
  const total = price * quantity;
  const message = "إجمالي فاتورتك لـ " + quantity + " من " + itemName + " هو " + total + " ريال.";

  console.log(message);
}

createReceipt("Saffron", 50, 2);
```

**الناتج:**
```
إجمالي فاتورتك لـ 2 من Saffron هو 100 ريال.
```