from utilities.save_load_data import load_data

def list_all_books():
    books = load_data()
    if not books:
        print("Knygų nėra.")
    else:
        for book in books:
            print(f"ID: {book.id} | Pavadinimas: {book.title} | Autorius: {book.author} | Metai: {book.release_date} | Žanras: {book.genre} | Kopijos: {book.total_copies} | Pasiskolinta: {len(book.borrowed_by)}")
