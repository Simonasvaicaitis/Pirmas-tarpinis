from classes.book import load_data, save_data

def return_book(book_id, user_name):
    books = load_data()
    found = False

    for book in books:
        if book.id == book_id:
            found = True
            # Ieškome tiksliai to paskolinimo įrašo pagal raktą "user"
            for record in book.borrowed_by:
                if record['user'] == user_name:
                    book.borrowed_by.remove(record)
                    save_data(books)
                    print(f"{user_name} grąžino knygą '{book.title}'.")
                    return
            # Jei esame radę knygą pagal ID, bet įrašo su tuo vartotoju nerandame:
            print(f"{user_name} neturi pasiskolinęs šios knygos.")
            return

    # Jei niekaip neįėjo į vidinį grąžinimo bloką, vadinasi knyga pagal ID nerasta
    if not found:
        print("Knyga nerasta.")