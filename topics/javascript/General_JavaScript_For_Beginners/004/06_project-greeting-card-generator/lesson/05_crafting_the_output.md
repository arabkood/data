الآن بعد أن أصبح لدينا الـ `message` المناسبة، لنجمع كل شيء مع `name` الشخص.

هل تتذكر **القوالب النصية (`template literals`)**؟ إنها مثالية لإنشاء نصوص سهلة القراءة تحتوي على متغيرات بداخلها.

سنستخدم الكلمة المفتاحية `return` لإرسال التهنئة النهائية المدمجة من دالتنا. هذا هو **الناتج الرئيسي** لمولّدنا.

```javascript
const createGreeting = (name, occasion) => {
  let message;

  if (occasion === 'Ramadan') {
    message = 'Ramadan Kareem!';
  } else if (occasion === 'Eid') {
    message = 'Eid Mubarak!';
  }

  return `مرحباً ${name}, ${message}`;
};
```