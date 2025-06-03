from classes.book import load_data

def search_by_title(title):
    books = load_data()
    matches = [book for book in books if title.lower() in book.title.lower()]
    if not matches:
        print("Nerasta knygų tokiu pavadinimu.")
    else:
        for book in matches:
            print(f"Pavadinimas: {book.title} | Autorius: {book.author} | Metai:({book.release_date})")