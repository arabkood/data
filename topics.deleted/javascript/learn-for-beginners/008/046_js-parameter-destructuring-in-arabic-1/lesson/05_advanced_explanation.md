# تقنيات متقدمة في التفكيك

التفكيك ليس مجرد استخراج للخصائص، بل يوفر مرونة أكبر:

### 1. إعطاء اسم مستعار (Aliasing)

أحيانًا، قد يكون اسم الخاصية غير مناسب كاسم للمتغير داخل الدالة. يمكنك إعادة تسميته هكذا:

```javascript
// نريد استخدام 'username' بدلاً من 'name'
function welcomeUser({ name: username }) {
  console.log(`مرحباً، ${username}`);
}

welcomeUser({ name: 'أحمد' }); // يطبع: مرحباً، أحمد
```

### 2. تحديد قيم افتراضية (Default Values)

ماذا لو لم تكن الخاصية موجودة في الكائن؟ يمكنك تحديد قيمة افتراضية لتجنب الحصول على `:undefined`.

```javascript
// إذا لم يتم توفير 'role'، سيتم استخدام 'user'
function createUser({ name, role = 'user' }) {
  console.log(`${name} لديه صلاحية ${role}`);
}

createUser({ name: 'سارة' }); // يطبع: سارة لديه صلاحية user
createUser({ name: 'خالد', role: 'admin' }); // يطبع: خالد لديه صلاحية admin
```