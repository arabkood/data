## مثال عملي: إطلاق الصاروخ 🚀

دعنا نطبق ما تعلمناه في مثال ممتع - برنامج العد التنازلي لإطلاق صاروخ!

```javascript
console.log("استعداد لإطلاق الصاروخ...");

for (let countdown = 5; countdown >= 1; countdown--) {
  console.log(`${countdown}...`);
}

console.log("🚀 انطلق الصاروخ!");
```

**النتيجة:**

```
استعداد لإطلاق الصاروخ...
5...
4...
3...
2...
1...
🚀 انطلق الصاروخ!
```

## تحليل الكود

1. **البداية**: `countdown = 5` (نبدأ العد من 5)
2. **الشرط**: `countdown >= 1` (نستمر حتى نصل إلى 1)
3. **التحديث**: `countdown--` (نقلل الرقم بواحد في كل مرة)

## تطوير المثال: إضافة تأخير وهمي

```javascript
console.log("🌟 مهمة إطلاق الصاروخ بدأت!");
console.log("جاري فحص الأنظمة...");

for (let system = 1; system <= 3; system++) {
  console.log(`✅ النظام ${system} جاهز`);
}

console.log("\n🚀 بدء العد التنازلي:");
for (let countdown = 10; countdown >= 1; countdown--) {
  if (countdown <= 3) {
    console.log(`🔥 ${countdown}...`);
  } else {
    console.log(`${countdown}...`);
  }
}

console.log("🚀💨 انطلق الصاروخ بنجاح!");
console.log("🌌 الصاروخ في طريقه إلى الفضاء!");
```

هذا المثال يجمع بين **حلقتين منفصلتين** و**جملة شرطية** لإنشاء تجربة أكثر واقعية!
