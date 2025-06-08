from utilities.save_load_data import load_data
from colorama import init, Fore, Style

def search_by_title(title):
    books = load_data()
    matches = [book for book in books if title.lower() in book.title.lower()]
    if not matches:
        print(f"{Fore.CYAN}Nerasta knygų tokiu pavadinimu.")
    else:
        for book in matches:
            print(f"{Fore.GREEN}Pavadinimas: {Fore.CYAN}{str(book.title):<35}"
                  f"{Fore.GREEN} | Autorius: {Fore.CYAN}{str(book.author):<25}"
                  f"{Fore.GREEN} | Metai: {Fore.CYAN}{str(book.release_date):<7}"
                  f"{Style.RESET_ALL}"
                  )