### 2. شاهد بنفسك: الكلمة المفتاحية `return`

تخيل دالة تحسب مجموع أسعار المنتجات في سلة التسوق. نحن لا نريد فقط أن *نرى* المجموع، بل نريد **استخدامه** في عملية الدفع.

الكلمة المفتاحية `return` هي الطريقة التي تُرجع بها الدالة قيمة معينة.

```javascript
function calculateTotal(price1, price2) {
  let total = price1 + price2;
  // هذا يرسل قيمة 'total' خارج الدالة
  return total; 
}

// القيمة المُرجعة يتم تخزينها الآن في 'finalPrice'
let finalPrice = calculateTotal(10, 25);

console.log(finalPrice);
```

**الناتج:**
```
35
```