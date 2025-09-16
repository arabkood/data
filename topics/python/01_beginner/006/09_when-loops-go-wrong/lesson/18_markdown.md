## تمرين تطبيقي: مدقق الحلقات

```python
# كود يحتوي على أخطاء متعددة - هل يمكنك إصلاحها؟

def find_max_in_list(numbers):
    """يجد أكبر رقم في القائمة"""
    if len(numbers) == 0:
        return None
    
    max_num = numbers[0]
    for i in range(1, len(numbers) + 1):  # خطأ محتمل؟
        if numbers[i] > max_num:
            max_num = numbers[i]
    
    return max_num

# اختبار
test_numbers = [3, 7, 2, 9, 1]
result = find_max_in_list(test_numbers)
print(f"أكبر رقم: {result}")
```

**هل تستطيع اكتشاف الخطأ قبل تشغيل الكود؟**

