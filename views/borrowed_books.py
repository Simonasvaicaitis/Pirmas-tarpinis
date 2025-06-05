from utilities.save_load_data import load_data

def list_borrowed_books():
    books = load_data()
    borrowed = False

    for book in books:
        if hasattr(book, 'borrowed_by') and book.borrowed_by:
            print(f"\nKnyga: {book.title} (ID: {book.id})")
            for record in book.borrowed_by:
                print(f" - Pasiskolino: {record['user']}, grąžinti iki {record['due_date']}")
            borrowed = True

    if not borrowed:
        print("Nėra paskolintų knygų.")