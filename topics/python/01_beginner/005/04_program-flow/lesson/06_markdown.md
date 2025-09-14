**تتبع حالة البرنامج**

المسار الذي يسلكه برنامجك يغير قيم المتغيرات. نسمي هذه القيم "حالة" (State) البرنامج. كمبرمج، يجب أن تكون قادراً على تتبع هذه الحالة في رأسك.

دعنا نتتبع "حالة" متغير `access_level` في هذا الكود:

```python
is_admin = False
is_moderator = True
access_level = 1 # الحالة الأولية

if is_admin:
  access_level = 3
elif is_moderator:
  access_level = 2 # الحالة تتغير هنا

# في هذه النقطة، قيمة access_level هي 2
```

لأن مسار `elif` هو الذي تم تنفيذه، تغيرت قيمة `access_level` من 1 إلى 2.
