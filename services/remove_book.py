from utilities.save_load_data import load_data, save_data

def remove_books_older_than(year):
    books = load_data()
    updated_books = [book for book in books if int(book.release_date.split('-')[0]) >= year]
    save_data(updated_books)