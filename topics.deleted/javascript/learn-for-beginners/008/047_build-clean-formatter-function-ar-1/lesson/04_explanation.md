# تجميع القطع معًا في دالة

لقد تعلمنا كيفية إزالة المسافات (`:trim()`) وتحويل الحرف الأول إلى كبير (`:toUpperCase()`). ولكن ماذا عن بقية الاسم؟ نريده أن يكون بأحرف صغيرة لتوحيد التنسيق.

يمكننا استخدام `:slice(1)` للحصول على كل شيء بعد الحرف الأول، ثم `:toLowerCase()` لتحويله إلى أحرف صغيرة.

> قبل أن نرى الكود النهائي، هل يمكنك تخمين كيف سنجمع `firstLetter` مع `restOfName`؟

لنرى كيف تبدو `:function` الكاملة:

```javascript
function formatName(name) {
  // 1. إزالة المسافات الزائدة
  const trimmedName = name.trim();

  // 2. تحويل الحرف الأول إلى كبير
  const firstLetter = trimmedName.charAt(0).toUpperCase();

  // 3. تحويل باقي الاسم إلى صغير
  const restOfName = trimmedName.slice(1).toLowerCase();

  // 4. دمج الجزئين معًا
  return firstLetter + restOfName;
}

console.log(formatName("  faRIS  ")); // الناتج: Faris
```

بإتقانك هذا المفهوم، أصبحت قادراً على إنشاء أدوات مساعدة قوية لتنظيف البيانات.