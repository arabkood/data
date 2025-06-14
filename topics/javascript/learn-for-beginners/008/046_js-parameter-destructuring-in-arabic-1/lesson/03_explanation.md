# الحل: تفكيك المعاملات (Parameter Destructuring)

ما رأيته في التمرين السابق يسمى `:parameter destructuring`. إنها طريقة في `:javascript` تسمح لك "بفك" أو استخراج الخصائص من `:object` أو عناصر من `:array` مباشرة في قائمة معاملات `:function`.

### الطريقة التقليدية مقابل التفكيك

**قبل (الطريقة التقليدية):**
```javascript
function printUserDetails(user) {
  const name = user.name;
  const city = user.city;
  console.log(`${name} من مدينة ${city}`);
}
```

**بعد (باستخدام التفكيك):**
```javascript
function printUserDetails({ name, city }) {
  console.log(`${name} من مدينة ${city}`);
}
```

لاحظ كيف أصبح الكود أقصر وأوضح. لقد قمنا بتعريف `:variables` `name` و `city` مباشرة في توقيع `:function`. الشرط الوحيد هو أن أسماء المتغيرات يجب أن تتطابق تمامًا مع أسماء الخصائص في الكائن.

> بإتقانك هذا المفهوم، أصبحت قادراً على كتابة دوال أكثر احترافية وقراءة، وهو ما يميز المطورين الخبراء.