التهنئة بـ 'العيد' تختلف عن التهنئة بـ 'التخرج'. هنا يأتي دور **المنطق الشرطي (`conditional logic`)**.

يمكننا استخدام جمل `if` و `else if` للتحقق من `المناسبة` وإعداد الرسالة الصحيحة.

لنقم بإعداد المنطق لمناسبتين: 'رمضان' و 'العيد'. سنقوم بتخزين الرسالة المحددة في متغير يسمى `message`.

```javascript
const createGreeting = (name, occasion) => {
  let message;

  if (occasion === 'Ramadan') {
    message = 'Ramadan Kareem!';
  } else if (occasion === 'Eid') {
    message = 'Eid Mubarak!';
  }

  // سنقوم بإرجاع التهنئة النهائية في الخطوة التالية
};
```