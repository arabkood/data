التعامل مع قاعدة أو قاعدتين هو خطوة أولى رائعة. لكن نظام التقييم الحقيقي يجب أن يتعامل مع كل الاحتمالات.

يمكننا ربط جمل `if`، و `else if`، و `else` الأخيرة معًا لإنشاء آلة متكاملة لاتخاذ القرارات.

**هذه الدالة تغطي الآن جميع التقديرات الرئيسية.**

```javascript
function getStudentGrade(student) {
  let score = student.score;

  if (score >= 90) {
    // ممتاز
    return "ممتاز";
  } else if (score >= 80) {
    // جيد جدا
    return "جيد جدا";
  } else if (score >= 70) {
    // جيد
    return "جيد";
  } else if (score >= 60) {
    // مقبول
    return "مقبول";
  } else {
    // راسب
    return "راسب";
  }
}

// لنجربها مع طالب اسمه خالد
let khalid = { name: "خالد", score: 76 };
console.log(getStudentGrade(khalid));
```

**الناتج:**

```
جيد
```

