from classes.book import load_data, save_data
from datetime import datetime, timedelta
from views.late_return_books import check_overdue_books

def borrow_book(book_id, user_name):
    books = load_data()
    if check_overdue_books(user_name):
        print(f"{user_name} turi negražintą vėluojančią knygą, daugiau skolinti negalima.")
        return

    for book in books:
        if book.id == book_id:
            if len(book.borrowed_by) < book.total_copies:
                due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
                book.borrowed_by.append({"Naudotojas": user_name, "gražinti iki": due_date})
                save_data(books)
                print(f"{user_name} pasiskolino '{book.title}' gražinti iki: {due_date}.")
                return
            else:
                print(f"'{book.title}' - Šios knygos kopijų neturime.")
                return
    print("Knyga nerasta.")