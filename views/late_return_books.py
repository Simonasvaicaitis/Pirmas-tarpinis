from utilities.save_load_data import load_data
from datetime import datetime
from services.orverdue import check_overdue_books
from colorama import init, Fore, Style

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