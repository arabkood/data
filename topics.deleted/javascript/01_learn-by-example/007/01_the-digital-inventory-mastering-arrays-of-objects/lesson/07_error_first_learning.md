لنلقِ نظرة على خطأ شائع. ما المشكلة في هذا الكود؟

```javascript
let sweets = [
  { name: "Kunafa", price: 30 },
  { name: "Baklava", price: 45 },
];

console.log(sweets.price);
```

```
undefined
```

يعيد الكود القيمة `undefined` لأن **`المصفوفة` نفسها لا تملك `خاصية` `price`**. يجب علينا أولاً اختيار `كائن` _من_ `المصفوفة` قبل أن نتمكن من الوصول إلى خصائصه.

