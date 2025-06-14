# من الفوضى إلى النظام: قوة الدوال

التسمية الجيدة هي نصف المعركة. النصف الآخر هو **البنية**. بدلاً من كتابة كود طويل ومكرر، يمكننا تجميعه في وحدات قابلة لإعادة الاستخدام تسمى الدوال `:functions`.

**كود فوضوي:**
```javascript
let price1 = 100;
let discount1 = 0.2;
let finalPrice1 = price1 - (price1 * discount1);

let price2 = 250;
let discount2 = 0.2;
let finalPrice2 = price2 - (price2 * discount2);
```

**بنية منظمة باستخدام `:function`:**
```javascript
function calculateFinalPrice(price, discount) {
  return price - (price * discount);
}

let finalPrice1 = calculateFinalPrice(100, 0.2);
let finalPrice2 = calculateFinalPrice(250, 0.2);
```
الكود الآن أقصر، أوضح، وأسهل للصيانة.