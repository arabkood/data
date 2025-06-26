إعطاء تعليمة واحدة أمر جيد، ولكن غالبًا ما نحتاج لتقديم المزيد.

لننشئ دالة لسجل الطلاب تحتاج إلى اسم وصف دراسي. يمكننا إضافة عدة `مُعامِلات` عن طريق فصلها بفاصلة.

```javascript
function describeStudent(name, grade) {
  console.log(name + " is in grade " + grade + ".");
}
```

**يجب أن يتطابق ترتيب تمرير الوسائط مع ترتيب المُعامِلات.**

```javascript
// "زيد" يطابق 'name'، و 9 تطابق 'grade'
describeStudent("Zayd", 9);

// --- المخرجات ---
// Zayd is in grade 9.
```