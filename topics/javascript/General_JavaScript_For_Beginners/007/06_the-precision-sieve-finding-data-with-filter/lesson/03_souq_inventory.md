فرز الأرقام مفيد، لكن القوة الحقيقية تظهر عند فرز مصفوفات الكائنات (`objects`). هذا شيء ستفعله طوال الوقت!

تخيل أن لدينا قائمة جرد لمتجر توابل إلكتروني. نريد أن نعرض للعميل فقط المنتجات المتوفرة حاليًا في المخزون.

لنلقِ نظرة على كيفية تعامل `filter` مع هذا الأمر باستخدام الكائنات.
```javascript
const souqInventory = [
  { name: 'Saffron', inStock: true },
  { name: 'Cardamom', inStock: false },
  { name: 'Rose Water', inStock: true }
];

const availableItems = souqInventory.filter(item => item.inStock === true);

console.log(availableItems);
// Output:
// [
//   { name: 'Saffron', inStock: true },
//   { name: 'Rose Water', inStock: true }
// ]
```
أرأيت؟ لقد طلبنا من `filter` ببساطة أن **يتحقق من خاصية `inStock`** لكل كائن. الأمر بهذه البساطة.