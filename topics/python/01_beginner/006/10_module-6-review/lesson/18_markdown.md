## 🎲 تحدي تفاعلي: لعبة التخمين المتقدمة

```python
import random

print("=== لعبة تخمين الرقم المتقدمة ===")
print("سأفكر في رقم من 1 إلى 100")

# إعداد اللعبة
secret_number = random.randint(1, 100)
max_attempts = 7
attempts = 0
game_over = False

# حلقة اللعب الرئيسية
while attempts < max_attempts and not game_over:
    attempts += 1
    remaining = max_attempts - attempts + 1
    
    print(f"\nالمحاولة {attempts}/{max_attempts} (متبقي: {remaining})")
    
    # الحصول على تخمين المستخدم
    while True:
        try:
            guess = int(input("تخمينك: "))
            if 1 <= guess <= 100:
                break
            else:
                print("يرجى إدخال رقم من 1 إلى 100")
        except ValueError:
            print("يرجى إدخال رقم صحيح")
    
    # تقييم التخمين
    if guess == secret_number:
        print(f"🎉 مبروك! خمنت الرقم {secret_number} في {attempts} محاولة!")
        game_over = True
    elif guess < secret_number:
        difference = secret_number - guess
        if difference <= 5:
            print("🔥 قريب جداً! الرقم أكبر قليلاً")
        elif difference <= 15:
            print("⬆️ الرقم أكبر")
        else:
            print("⬆️⬆️ الرقم أكبر بكثير")
    else:
        difference = guess - secret_number
        if difference <= 5:
            print("🔥 قريب جداً! الرقم أصغر قليلاً")
        elif difference <= 15:
            print("⬇️ الرقم أصغر")
        else:
            print("⬇️⬇️ الرقم أصغر بكثير")

# نهاية اللعبة
if not game_over:
    print(f"\n😔 انتهت المحاولات! الرقم كان {secret_number}")

print("\nشكراً لك على اللعب!")
```

