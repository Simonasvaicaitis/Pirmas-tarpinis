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
        try:
            print("\nBibliotekos meniu:")
            print("1. Pridėti knygą")
            print("2. Pašalinti nenaudojamas knygas, senesnes nei: ")
            print("3. Pasiskolinti knygą")
            print("4. Ieškoti pagal pavadinimą")
            print("5. Ieškoti pagal autorių")
            print("6. Visų knygų sąrašas")
            print("7. Vėluojančių knygų sąrašas")
            print("8. Paskolintų knygų sąrašas")
            print("9. Grąžinti knygą")
            print("0. Baigti programą")

            choice = input("Pasirinkite ką norite atlikti: ")

            if choice == '1':
                try:
                    title = input("Pavadinimas: ")
                    author = input("Autorius: ")
                    release = input("Išleidimo metai (YYYY): ")
                    genre = input("Žanras: ")
                    copies = int(input("Kopijų: "))
                    add_book(title, author, release, genre, copies)
                except KeyboardInterrupt as e:
                    print(f"Klaida. {e}")
                except Exception as e:
                    print(f"Klaida pridedant knygą: {e}")

            elif choice == '2':
                try:
                    year = int(input("Įveskite metus (pvz. 2000): "))
                    remove_books_older_than(year)
                    print(f"Knygos, senesnės nei {year}, buvo pašalintos.")
                except KeyboardInterrupt as e:
                    print(f"Klaida. {e}")
                except Exception as e:
                    print(f"Klaida, bandykite dar kartą: {e}")

            elif choice == '3':
                try:
                    book_id = input("Įvesti knygos ID: ")
                    user = input("Jūsų vardas: ")
                    borrow_book(book_id, user)
                except KeyboardInterrupt as e:
                    print(f"Klaida. {e}")
                except Exception as e:
                    print(f"Klaida, bandykite dar kartą: {e}")

            elif choice == '4':
                try:
                    title = input("Įvesti pavadinimą: ")
                    search_by_title(title)
                except KeyboardInterrupt as e:
                    print(f"Klaida. {e}")
                except Exception as e:
                    print(f"Klaida, bandykite dar kartą: {e}")

            elif choice == '5':
                try:
                    author = input("Įvesti autorių: ")
                    search_by_author(author)
                except KeyboardInterrupt as e:
                    print(f"Klaida. {e}")
                except Exception as e:
                    print(f"Klaida, bandykite dar kartą: {e}")

            elif choice == '6':
                try:
                    print("Knygų sąrašas:")
                    list_all_books()
                except KeyboardInterrupt as e:
                    print(f"Klaida. {e}")
                except Exception as e:
                    print(f"Klaida, bandykite dar kartą: {e}")

            elif choice == '7':
                try:
                    print("Vėluojančių knygų sąrašas:")
                    list_overdue_books()
                except KeyboardInterrupt as e:
                    print(f"Klaida. {e}")
                except Exception as e:
                    print(f"Klaida, bandykite dar kartą: {e}")
            
            elif choice == '8':
                try:
                    print("Paskolintų knygų sąrašas:")
                    list_borrowed_books()
                except KeyboardInterrupt as e:
                    print(f"Klaida. {e}")
                except Exception as e:
                    print(f"Klaida, bandykite dar kartą: {e}")
            
            elif choice == '9':
                try:
                    book_id = input("Įveskite knygos ID: ")
                    user = input("Jūsų vardas: ")
                    return_book(book_id, user)
                except KeyboardInterrupt as e:
                    print(f"Klaida. {e}")
                except Exception as e:
                    print(f"Klaida, bloga įvestis: {e}")

            elif choice == '0':
                print("Programa baigta.")
                break

            else:
                print("Blogas pasirinkimas, bandykite dar kartą.")
        except KeyboardInterrupt as e:
            print(f"Klaida. {e}")
        except Exception as e:
            print(f"Klaida, bandykite dar kartą: {e}")

if __name__ == "__main__":
    main()