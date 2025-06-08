from utilities.save_load_data import load_data
from colorama import init, Fore, Style

def list_all_books():
    books = load_data()
    if not books:
        print(f"{Fore.CYAN}Knygų nėra."
              f"{Style.RESET_ALL}"
              )
    else:
        for book in books:
            print(
                f"{Fore.GREEN}ID: {Fore.CYAN}{str(book.id):<32}"
                f"{Fore.GREEN} | Pavadinimas: {Fore.CYAN}{str(book.title):<35}"
                f"{Fore.GREEN} | Autorius: {Fore.CYAN}{str(book.author):<25}"
                f"{Fore.GREEN} | Metai: {Fore.CYAN}{str(book.release_date):<7}"
                f"{Fore.GREEN} | Žanras: {Fore.CYAN}{str(book.genre):<20}"
                f"{Fore.GREEN} | Kopijos: {Fore.CYAN}{str(book.total_copies):<5}"
                f"{Fore.GREEN} | Pasiskolinta: {Fore.CYAN}{len(book.borrowed_by)}"
                f"{Style.RESET_ALL}"
            )