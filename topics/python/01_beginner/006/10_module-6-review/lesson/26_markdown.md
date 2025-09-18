## 🌟 مشاريع تطبيقية للممارسة

إذا كنت تريد ممارسة أكثر، جرب هذه المشاريع:

### 1. مولد كلمات المرور:
```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    password = ""
    
    for i in range(length):
        password += random.choice(characters)
    
    return password

# اختبار
for i in range(1, 6):
    print(f"كلمة مرور {i*2} حرف: {generate_password(i*2)}")
```

### 2. محلل النصوص:
```python
def analyze_text(text):
    # إحصائيات أساسية
    total_chars = len(text)
    total_words = len(text.split())
    total_sentences = text.count('.') + text.count('!') + text.count('?')
    
    # تحليل الأحرف
    letters = 0
    digits = 0
    spaces = 0
    
    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char == ' ':
            spaces += 1
    
    # النتائج
    print(f"=== تحليل النص ===")
    print(f"إجمالي الأحرف: {total_chars}")
    print(f"عدد الكلمات: {total_words}")
    print(f"عدد الجمل: {total_sentences}")
    print(f"الأحرف: {letters}")
    print(f"الأرقام: {digits}")
    print(f"المسافات: {spaces}")
    
    if total_words > 0:
        avg_word_length = (letters / total_words)
        print(f"متوسط طول الكلمة: {avg_word_length:.1f}")
```

### 3. آلة حاسبة الإحصائيات:
```python
def calculate_statistics(numbers):
    if not numbers:
        return "القائمة فارغة!"
    
    # الحسابات الأساسية
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    # أكبر وأصغر قيمة
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    # عد الموجب والسالب
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    return {
        "المجموع": total,
        "العدد": count, 
        "المتوسط": round(average, 2),
        "الأكبر": maximum,
        "الأصغر": minimum,
        "الموجبة": positive_count,
        "السالبة": negative_count,
        "الصفر": zero_count
    }
```

