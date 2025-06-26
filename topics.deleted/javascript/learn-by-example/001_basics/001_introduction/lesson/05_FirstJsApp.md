## شغّل أول برنامج جافاسكربت لك!

1. أنشئ ملفًا باسم `hello.js`
2. انسخ هذا الكود داخل الملف:

```javascript title="hello.js"
const now = new Date();
const hour = now.getHours();

const yourName = "محمد";

if (hour < 12) {
  console.log(`صباح الخير، ${yourName}!`);
} else {
  console.log(`مساء الخير، ${yourName}!`);
}
```

3. افتح `:terminal` وتأكد أنك داخل المجلد الذي يحتوي على الملف، ثم اكتب:

```bash
node hello.js
```

> [!NOTE]
> استخدم الأمر `cd` للانتقال إلى المجلد الذي يحتوي على الملف. مثلاً:
