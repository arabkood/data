لنكتشف كيفية إصلاح مشكلة خفيّة وغير مرئية: المسافات الزائدة!

أحيانًا يضيف المستخدمون مسافات عن طريق الخطأ قبل أو بعد مدخلاتهم. هذا يمكن أن يسبب مشاكل.

```javascript
let correctCode = "1991";
let userEntry = " 1991 ";

console.log(correctCode === userEntry);
```

**الناتج**

```
false
```

يا لهذه الخدعة! المسافات تجعل الحاسوب يراهما مختلفتين. يمكننا استخدام دالة `trim()` **لإزالة المسافات البيضاء من كلا طرفي** النص.

```javascript
let correctCode = "1991";
let userEntry = " 1991 ";

console.log(correctCode.trim() === userEntry.trim());
```

**الناتج**

```
true
```

