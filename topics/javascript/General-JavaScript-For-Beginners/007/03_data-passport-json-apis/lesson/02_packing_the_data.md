لنبدأ بكائن جافاسكريبت مألوف لمستخدم اسمه عمر.

```javascript
// كائن جافاسكريبت الخاص بنا
const userObject = {
  name: "Omar",
  isStudent: true,
  courses: ["Math", "History"]
};
```

لتحويل هذا إلى سلسلة نصية بصيغة `JSON`، نستخدم أداة مدمجة: `JSON.stringify()`.

```javascript
// الآن أصبح سلسلة نصية بصيغة JSON!
const jsonString = JSON.stringify(userObject);

console.log(jsonString);
```

**الناتج:**
```
{"name":"Omar","isStudent":true,"courses":["Math","History"]}
```

هل لاحظت الفروقات الصغيرة ولكن المهمة؟ في سلسلة `JSON` النصية، **جميع المفاتيح مثل `"name"` تكون أيضًا بين علامتي اقتباس مزدوجتين**.