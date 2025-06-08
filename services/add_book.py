from utilities.save_load_data import load_data, save_data
from classes.inventory import Inventory
from colorama import init, Fore, Style

def add_book(title, author, release_date, genre, copies):
    books = load_data()
    book = Inventory(title, author, release_date, genre, copies)
    books.append(book)
    save_data(books)
    print(f"{Fore.CYAN}Knyga '{title}' pridėta, {copies} kopijos."
          f"{Style.RESET_ALL}"
          )