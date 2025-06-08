from utilities.save_load_data import load_data
from colorama import init, Fore, Style

def list_borrowed_books():
    books = load_data()
    borrowed = False

    for book in books:
        if hasattr(book, 'borrowed_by') and book.borrowed_by:
            print(f"{Fore.CYAN}\nKnyga: {book.title} (ID: {book.id})"
                  f"{Style.RESET_ALL}"
                  )
            for record in book.borrowed_by:
                print(f"{Fore.CYAN} - Pasiskolino: {record['user']:<20} Gražinti iki {record['due_date']}"
                      f"{Style.RESET_ALL}"
                      )
            borrowed = True

    if not borrowed:
        print(f"{Fore.CYAN}Nėra paskolintų knygų."
              f"{Style.RESET_ALL}"
              )