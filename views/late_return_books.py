from utilities.save_load_data import load_data
from datetime import datetime
from colorama import init, Fore, Style

def check_overdue_books(user=None):
    books = load_data()
    overdue_books = []

    for book in books:
        for record in book.borrowed_by:
            try:
                due_date = datetime.strptime(record['due_date'], "%Y-%m-%d")
            except (KeyError, ValueError):
                continue

            if due_date < datetime.now():
                if user:
                    if record['user'] == user:
                        return True
                    continue
                overdue_books.append((book.title, record['user'], record['due_date']))

    if user:
        return False
    return overdue_books

def list_overdue_books():
    overdue = check_overdue_books()
    if not overdue:
        print(f"{Fore.CYAN}Nėra vėluojančių knygų."
              f"{Style.RESET_ALL}"
              )
        return

    print(f"{Fore.CYAN}Vėluojančios knygos: "
          f"{Style.RESET_ALL}"
          )
    for book_title, user, due_date in overdue:
        print(f"{Fore.MAGENTA}Pavadinimas: {str(book_title):<35}"
              f"Knygą pasiskolino: {str(user):<30}"
              f"Gražinti iki: {str(due_date):<13}"
              f"{Style.RESET_ALL}"
              )