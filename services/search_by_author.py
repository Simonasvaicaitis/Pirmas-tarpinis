from classes.book import load_data

def search_by_author(author):
    books = load_data()
    matches = [book for book in books if author.lower() in book.author.lower()]
    if not matches:
        print("Šio autoriaus knygų nerasta.")
    else:
        for book in matches:
            print(f"Pavadinimas: {book.title} | Autorius: {book.author} | Metai:({book.release_date})")

