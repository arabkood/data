### ٤. مَصنَع الدوال

يمكن لـ`الدوال عالية الرتبة` أيضًا أن **تُرجع دالة جديدة**. فكّر في الأمر كأنه مصنع.

تطلب من المصنع أداة معينة، فيقوم ببنائها ويسلمها لك.

```javascript
// هذه هي دالة 'المصنع' الخاصة بنا
function createGreeting(greetingWord) {
  // إنها تُرجع دالة جديدة تمامًا
  return function(name) {
    console.log(greetingWord + "، " + name);
  };
}

// لننشئ أداتي ترحيب مختلفتين
const sayAhlan = createGreeting("أهلاً");
const saySalam = createGreeting("سلام");

// الآن، لنستخدم أدواتنا الجديدة!
sayAhlan("خالد");
saySalam("فاطمة");
```

**المُخرجات:**
```
أهلاً، خالد
سلام، فاطمة
```