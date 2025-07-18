// هذا السكريبت يُنشئ لافتة ترحيب للاعب.
player_name = "طه"
player_class = محارب
player_level = 5

# إنشاء الحدود العلوية والسفلية
border_char = "*"
    border_length = "30"
full_border = border_char * border_length

# إنشاء رسائل الترحيب
message_1 = "مرحباً بك يا " + player_class + " " + player_name + "!"
message_2 = "أنت تبدأ من المستوى "   str(player_level)

# طباعة اللافتة النهائية
Print[full_border]
print(message_1
print(message_2)
print(full_border)
