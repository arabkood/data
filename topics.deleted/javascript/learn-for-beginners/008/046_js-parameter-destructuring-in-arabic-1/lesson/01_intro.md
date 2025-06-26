# مشكلة شائعة: الوصول المتكرر لخصائص الكائن

عندما نمرر `:object` كـ `:parameter` إلى `:function`، غالبًا ما نجد أنفسنا نكرر اسم الكائن للوصول إلى خصائصه. انظر إلى هذا المثال:

```javascript
const user = {
  name: 'نورة',
  age: 28,
  city: 'الرياض'
};

function displayUser(user) {
  const name = user.name;
  const age = user.age;
  console.log(`${name} عمره(ا) ${age} سنة.`);
}

displayUser(user);
```

الكود يعمل، لكن هل هناك طريقة أذكى وأقصر للوصول إلى `name` و `age` مباشرة داخل تعريف `:function`؟

> قبل أن نكمل، فكّر في كيف يمكن تبسيط هذا الكود. هذا التفكير سيجهز عقلك للمفهوم القادم.