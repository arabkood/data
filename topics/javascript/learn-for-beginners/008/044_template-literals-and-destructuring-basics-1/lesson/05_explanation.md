# استخراج البيانات بأناقة: التفكيك (`Destructuring`)

عندما نتعامل مع كائنات (`:object`)، غالبًا ما نحتاج إلى استخراج خصائصها في متغيرات منفصلة. التفكيك هو اختصار أنيق للقيام بذلك.

**الطريقة التقليدية:**
```javascript
const user = { name: "علي", city: "الرياض" };
const userName = user.name; // "علي"
const userCity = user.city; // "الرياض"
```

**باستخدام التفكيك:**
```javascript
const user = { name: "علي", city: "الرياض" };

// استخراج خاصية name و city في متغيرات بنفس الاسم
const { name, city } = user;

console.log(name); // "علي"
console.log(city); // "الرياض"
```
هذا يجعل الكود أقصر وأوضح!