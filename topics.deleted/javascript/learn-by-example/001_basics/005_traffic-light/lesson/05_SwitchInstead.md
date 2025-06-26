# البديل الأنيق: switch

تذكر مثال إشارة المرور من المثال السابق؟ عندما نريد مقارنة متغير واحد بعدة قيم مختلفة، هناك طريقة أكثر أناقة من استخدام عدة `:else if`.

**switch** مثل قائمة خيارات: نعطي المتغير، ونقول "إذا كان كذا، افعل كذا".

## المقارنة: else if مقابل switch

```javascript
// الطريقة القديمة - else if
const lightColor = "أصفر";

if (lightColor === "أحمر") {
  console.log("قف! 🛑");
} else if (lightColor === "أصفر") {
  console.log("استعد للتوقف ⚠️");
} else if (lightColor === "أخضر") {
  console.log("تحرك 🚦");
}

// الطريقة الجديدة - switch
switch (lightColor) {
  case "أحمر":
    console.log("قف! 🛑");
    break;
  case "أصفر":
    console.log("استعد للتوقف ⚠️");
    break;
  case "أخضر":
    console.log("تحرك 🚦");
    break;
  default:
    console.log("إشارة غير معروفة");
}
```

## عناصر switch الأساسية

- **switch()**: نضع المتغير الذي نريد فحصه
- **case**: كل احتمال ممكن للقيمة
- **break**: يوقف التنفيذ (مهم جداً!)
- **default**: الحالة الافتراضية (مثل `:else:`)

⚠️ **لا تنس break!** بدونها، سيستمر الكود في تنفيذ باقي الحالات.
