## أخطاء شائعة في الحلقات وكيفية تجنبها

## 1. الحلقة اللانهائية ⚠️

**الخطأ:**

```javascript
let i = 1;
while (i <= 5) {
  console.log(i);
  // نسيت زيادة i!
}
// هذه الحلقة لن تتوقف أبداً
```

**الحل:**

```javascript
let i = 1;
while (i <= 5) {
  console.log(i);
  i++; // تذكر تحديث المتغير!
}
```

## 2. خطأ في شرط الإيقاف

**الخطأ:**

```javascript
for (let i = 1; i < 5; i++) {
  console.log(i);
}
// يطبع: 1, 2, 3, 4 (لا يطبع 5)
```

**إذا أردت طباعة 5 أيضاً:**

```javascript
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
// يطبع: 1, 2, 3, 4, 5
```

## 3. استخدام متغير خارج نطاق الحلقة

**الخطأ:**

```javascript
for (let count = 1; count <= 3; count++) {
  console.log(count);
}
console.log(count); // خطأ! count غير موجود هنا
```

**الحل:**

```javascript
let count;
for (count = 1; count <= 3; count++) {
  console.log(count);
}
console.log(`آخر قيمة: ${count}`); // الآن يعمل
```

## 4. الخلط بين ++ و --

```javascript
// للعد التصاعدي
for (let i = 1; i <= 5; i++) { ... }

// للعد التنازلي
for (let i = 5; i >= 1; i--) { ... }
```

## نصيحة ذهبية ✨

**اختبر حلقتك دائماً بقيم صغيرة أولاً!** إذا أردت حلقة تعد إلى 1000، جربها أولاً بالعد إلى 5 للتأكد من أنها تعمل بشكل صحيح.
