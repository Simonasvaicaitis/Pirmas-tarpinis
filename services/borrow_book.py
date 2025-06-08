from utilities.save_load_data import load_data, save_data
from datetime import datetime, timedelta
from views.late_return_books import check_overdue_books
from colorama import init, Fore, Style

def borrow_book(book_id, user_name):
    books = load_data()

    if check_overdue_books(user_name):
        print(f"{Fore.CYAN}{user_name} turi negražintą vėluojančią knygą, daugiau skolinti negalima.")
        return

    found_book = None
    for b in books:
        if b.id == book_id:
            found_book = b
            break

    if not found_book:
        print("Knyga nerasta.")
        return

    book = found_book

    if len(book.borrowed_by) >= book.total_copies:
        print(f"'{book.title}', šios knygos kopijų šiuo metu nėra.")
        return

    due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
    book.borrowed_by.append({"user": user_name, "due_date": due_date})
    save_data(books)
    print(f"{user_name} pasiskolino '{book.title}', gražinti iki: {due_date}."
          f"{Style.RESET_ALL}"
          )