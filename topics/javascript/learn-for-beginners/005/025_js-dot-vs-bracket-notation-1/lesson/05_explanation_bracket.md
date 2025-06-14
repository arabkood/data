# الطريقة الثانية: تدوين الأقواس (`[]`)

ممتاز! لقد اكتشفت الحاجة إلى **تدوين الأقواس**.

نستخدمها في حالتين أساسيتين:

**1. عندما يحتوي اسم الخاصية على مسافات أو رموز خاصة:**

```javascript
const settings = {
  "user-id": 12345
};
// console.log(settings.user-id); // هذا سيسبب خطأ!
console.log(settings["user-id"]); // صحيح! الناتج: 12345
```

**2. عندما يكون اسم الخاصية متغيرًا (وصول ديناميكي):**

تخيل أنك تريد الوصول إلى خاصية، لكن اسمها مخزن في `:variable` آخر.

```javascript
const person = {
  city: "Riyadh",
  country: "Saudi Arabia"
};

let keyToAccess = "city";
console.log(person[keyToAccess]); // الناتج: Riyadh
```

لا يمكن فعل ذلك باستخدام تدوين النقطة (`person.keyToAccess` ستبحث عن خاصية اسمها `keyToAccess` حرفيًا).