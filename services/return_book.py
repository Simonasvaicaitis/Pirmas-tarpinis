from classes.book import load_data, save_data

def return_book(book_id, user_name):
    books = load_data()
    found = False

    for book in books:
        if book.id == book_id:
            for record in book.borrowed_by:
                if record['user'] == user_name:
                    book.borrowed_by.remove(record)
                    save_data(books)
                    print(f"{user_name} grąžino knygą '{book.title}'.")
                    found = True
                    return
            print(f"{user_name} neturi pasiskolinęs šios knygos.")
            return

    if not found:
        print("Knyga nerasta.")