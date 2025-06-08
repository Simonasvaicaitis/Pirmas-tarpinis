from utilities.save_load_data import load_data, save_data
from colorama import init, Fore, Style

def return_book(book_id, user_name):
    books = load_data()

    book = None
    for b in books:
        if b.id == book_id:
            book = b
            break

    if not book:
        print(f"{Fore.CYAN}Knyga nerasta.")
        return

    found_record = None
    for record in book.borrowed_by:
        if record.get('user') == user_name:
            found_record = record
            break

    if not found_record:
        print(f"{user_name} neturi pasiskolinęs šios knygos.")
        return

    book.borrowed_by.remove(found_record)
    save_data(books)
    print(f"{user_name} grąžino knygą '{book.title}'."
          f"{Style.RESET_ALL}"
          )