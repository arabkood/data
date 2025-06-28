`&&`: المُعامِل `AND` (`و`)

يتحقق المُعامِل `&&` مما إذا كانت الشروط على **كلا الجانبين** `true`. إذا كان أحدها فقط `false`، فإن التعبير بأكمله يصبح `false`.

فكّر بالأمر كأنك تحتاج لمفتاحين لفتح صندوق كنز.

```javascript
let hasHighMarks = true;
let hasGoodInterview = false;

// يجب أن يكون كلا الشرطين صحيحين للحصول على نتيجة `true`
console.log(hasHighMarks && hasGoodInterview);
```

**الناتج:**

```
false
```

لأن `hasGoodInterview` قيمتها `false`، فإن الشرط بأكمله يُقيَّم إلى `false`.

