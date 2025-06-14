# مثال عملي: الحفاظ على خصوصية البيانات

أحد الاستخدامات الشائعة للـ`:closure` هو إنشاء "متغيرات خاصة" (`:private variables`) لا يمكن الوصول إليها أو تعديلها مباشرة من خارج الدالة، مما يجعل كودك أكثر أمانًا وموثوقية.

```javascript
function createPerson(name) {
  let age = 0; // متغير "خاص"

  return {
    getName: function() {
      return name; // الوصول لـ name من الدالة الخارجية
    },
    getAge: function() {
      return age; // الوصول لـ age من الدالة الخارجية
    },
    celebrateBirthday: function() {
      age++;
      console.log(`عيد ميلاد سعيد يا ${name}! عمرك الآن ${age}.`);
    }
  };
}

const user = createPerson("علي");
// لا يمكننا الوصول إلى 'age' مباشرة:
// console.log(user.age); // سيعطي undefined

user.celebrateBirthday(); // "عيد ميلاد سعيد يا علي! عمرك الآن 1."
```

> بإتقانك هذا المفهوم، أصبحت قادراً على تصميم وحدات (`:modules`) برمجية تحمي بياناتها بنفسها، وهي ممارسة أساسية في هندسة البرمجيات الحديثة.