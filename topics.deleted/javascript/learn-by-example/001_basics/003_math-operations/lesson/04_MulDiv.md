## ✖️ الضرب و ➗ القسمة

الآن، لنتعرف على عمليتي الضرب والقسمة. جافاسكريبت تجعل هذه العمليات سهلة للغاية.

### 1. الضرب (`*`)

تستخدم علامة النجمة `*` (تسمى Asterisk) لضرب الأرقام.

```javascript
let length = 4;
let width = 6;
let area = length * width;
console.log("مساحة المستطيل: " + area);
// مساحة المستطيل: 24
```

### 2. القسمة (`/`)

تستخدم علامة الشرطة المائلة `/` (Forward Slash) لقسمة رقم على آخر.

```javascript
let totalCandies = 20;
let numberOfChildren = 4;
let candiesPerChild = totalCandies / numberOfChildren; // الناتج سيكون 5

console.log("إجمالي الحلوى: " + totalCandies);
// إجمالي الحلوى: 20
console.log("عدد الأطفال: " + numberOfChildren);
// عدد الأطفال: 4
console.log("نصيب كل طفل: " + candiesPerChild + " قطع حلوى.");
// نصيب كل طفل: 5 قطع حلوى.

// ماذا عن الأرقام غير القابلة للقسمة بالتساوي؟
let pizzaSlices = 10;
let people = 3;
let slicesPerPerson = pizzaSlices / people;
console.log("شرائح البيتزا لكل شخص: " + slicesPerPerson);
// شرائح البيتزا لكل شخص: 3.3333333333333335
```

جافاسكريبت تتعامل مع الأرقام العشرية (الكسور) تلقائيًا عند الحاجة!
