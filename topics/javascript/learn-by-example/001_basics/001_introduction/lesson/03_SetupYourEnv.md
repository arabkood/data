## 🚀 ابدأ مع `JavaScript` على حاسوبك (سهل جداً!)

هل تريد تشغيل `JavaScript` على حاسوبك الشخصي؟ اتبع هذه الخطوات السريعة!

---

## 1️⃣ تثبيت `Node.js`

👈 اذهب إلى [https://nodejs.org](https://nodejs.org)

- قم بتنزيل **إصدار الدعم طويل الأمد (LTS)**
- افتح الملف وانقر على **التالي** (Next) حتى ينتهي التثبيت

---

## 2️⃣ تحقق مما إذا كان يعمل

افتح `:terminal` (قد يُسمى حسب نظامك: `Command Prompt`، أو `Terminal`، أو `PowerShell`) ثم اكتب:

```bash
node -v
```

يجب أن ترى رقم إصدار مشابه لـ:

```
v22.16.0
```

هذا يعني أنه يعمل!

---

## 3️⃣ شغّل أول برنامج `JavaScript` لك

1. أنشئ ملفًا باسم `hello.js`
2. انسخ هذا الكود داخل الملف:

```javascript
const now = new Date();
const hour = now.getHours();

const yourName = "محمد";

if (hour < 12) {
  console.log(`صباح الخير، ${yourName}!`);
} else {
  console.log(`مساء الخير، ${yourName}!`);
}
```

3. افتح `:terminal` **وتأكد أنك داخل المجلد الذي يحتوي على الملف**، ثم اكتب:

```bash
node hello.js
```

📝 **معلومة مهمة:**
استخدم الأمر `cd` للانتقال إلى المجلد الذي يحتوي على الملف. مثلاً:

```bash
cd Desktop
```
