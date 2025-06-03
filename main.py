from services.add_book import add_book
from services.remove_book import remove_books_older_than
from services.borrow_book import borrow_book
from services.search_by_title import search_by_title
from services.search_by_author import search_by_author
from views.all_books import list_all_books
from views.late_return_books import list_overdue_books
from views.borrowed_books import list_borrowed_books
from services.return_book import return_book

import pickle

# with open('data/library.pickle', 'wb') as f:
#     pickle.dump([], f)

def main():
    while True:
        print("\n--- Bibliotekos valdymas ---")
        print("1. Pridėti knygą")
        print("2. Pašalinti knygas iki nurodytų metų")
        print("3. Pasiskolinti knygą")
        print("4. Grąžinti knygą")
        print("5. Ieškoti pagal pavadinimą")
        print("6. Ieškoti pagal autorių")
        print("7. Rodyti visas knygas")
        print("8. Rodyti paskolintas knygas")
        print("9. Rodyti vėluojančias knygas")
        print("0. Išeiti")

        choice = input("Pasirinkite veiksmą: ")

        if choice == '1':
            title = input("Pavadinimas: ")
            author = input("Autorius: ")
            release = input("Išleidimo data (YYYY-MM-DD): ")
            genre = input("Žanras: ")
            copies = int(input("Egzempliorių skaičius: "))
            add_book(title, author, release, genre, copies)

        elif choice == '2':
            year = int(input("Nuo kurių metų laikyti? "))
            remove_books_older_than(year)

        elif choice == '3':
            book_id = input("Įveskite knygos ID: ")
            user = input("Jūsų vardas: ")
            borrow_book(book_id, user)

        elif choice == '4':
            book_id = input("Įveskite knygos ID: ")
            user = input("Jūsų vardas: ")
            return_book(book_id, user)

        elif choice == '5':
            title = input("Įveskite pavadinimą: ")
            search_by_title(title)

        elif choice == '6':
            author = input("Įveskite autorių: ")
            search_by_author(author)

        elif choice == '7':
            list_all_books()

        elif choice == '8':
            list_borrowed_books()

        elif choice == '9':
            list_overdue_books()

        elif choice == '0':
            break

        else:
            print("Neteisingas pasirinkimas.")

if __name__ == "__main__":
    main()