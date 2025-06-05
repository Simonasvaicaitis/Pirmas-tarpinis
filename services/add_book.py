from classes.book import load_data, save_data
from classes.inventory import Inventory

def add_book(title, author, release_date, genre, copies):
    books = load_data()
    book = Inventory(title, author, release_date, genre, copies)
    books.append(book)
    save_data(books)
    print(f"Knyga '{title}' pridėta, {copies} kopijos.")
