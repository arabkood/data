## 🏆 اختبار نهائي شامل

دعنا نختبر فهمك لجميع مفاهيم الوحدة في تحدي واحد:

**المطلوب:** اكتب برنامج لإدارة مكتبة بسيطة يمكنه:
1. إضافة كتب جديدة
2. البحث عن كتاب
3. عرض جميع الكتب
4. حساب إحصائيات (عدد الكتب، أطول عنوان، إلخ)

```python
# قاعدة بيانات الكتب
library = []

def add_book():
    title = input("عنوان الكتاب: ")
    author = input("المؤلف: ")
    pages = int(input("عدد الصفحات: "))
    
    book = {
        "title": title,
        "author": author, 
        "pages": pages
    }
    library.append(book)
    print(f"تم إضافة '{title}' بنجاح!")

def search_books():
    search_term = input("ابحث عن: ").lower()
    found_books = []
    
    for book in library:
        if (search_term in book["title"].lower() or 
            search_term in book["author"].lower()):
            found_books.append(book)
    
    if found_books:
        print(f"وُجد {len(found_books)} كتاب:")
        for book in found_books:
            print(f"- {book['title']} للمؤلف {book['author']}")
    else:
        print("لم يوجد كتب مطابقة")

def show_statistics():
    if not library:
        print("المكتبة فارغة!")
        return
    
    total_books = len(library)
    total_pages = 0
    longest_title = ""
    authors = []
    
    for book in library:
        total_pages += book["pages"]
        if len(book["title"]) > len(longest_title):
            longest_title = book["title"]
        if book["author"] not in authors:
            authors.append(book["author"])
    
    average_pages = total_pages / total_books
    
    print(f"=== إحصائيات المكتبة ===")
    print(f"عدد الكتب: {total_books}")
    print(f"إجمالي الصفحات: {total_pages}")
    print(f"متوسط الصفحات: {average_pages:.1f}")
    print(f"أطول عنوان: {longest_title}")
    print(f"عدد المؤلفين: {len(authors)}")

# برنامج رئيسي
while True:
    print("\n=== مكتبتي ===")
    print("1. إضافة كتاب")
    print("2. البحث عن كتاب") 
    print("3. عرض جميع الكتب")
    print("4. إحصائيات")
    print("5. خروج")
    
    choice = input("اختيارك: ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        search_books()
    elif choice == "3":
        if library:
            for i, book in enumerate(library, 1):
                print(f"{i}. {book['title']} - {book['author']} ({book['pages']} صفحة)")
        else:
            print("المكتبة فارغة!")
    elif choice == "4":
        show_statistics()
    elif choice == "5":
        print("شكراً لاستخدام المكتبة!")
        break
    else:
        print("خيار غير صحيح!")
```

