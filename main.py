from services.add_book import add_book
from services.remove_book import remove_books_older_than
from services.borrow_book import borrow_book
from services.search_by_title import search_by_title
from services.search_by_author import search_by_author
from views.all_books import list_all_books
from views.late_return_books import list_overdue_books
from views.borrowed_books import list_borrowed_books
from services.return_book import return_book
from colorama import init, Fore, Style

import pickle

# with open('data/library.pickle', 'wb') as f:
#     pickle.dump([], f)

def main():
    init(autoreset=True)
    while True:
        try:
            print(f"{Fore.GREEN}\nBibliotekos meniu:")
            print(f"{Fore.YELLOW}1. Pridėti knygą")
            print(f"{Fore.YELLOW}2. Pašalinti nenaudojamas knygas, senesnes nei: ")
            print(f"{Fore.YELLOW}3. Pasiskolinti knygą")
            print(f"{Fore.YELLOW}4. Ieškoti pagal pavadinimą")
            print(f"{Fore.YELLOW}5. Ieškoti pagal autorių")
            print(f"{Fore.YELLOW}6. Visų knygų sąrašas")
            print(f"{Fore.YELLOW}7. Vėluojančių knygų sąrašas")
            print(f"{Fore.YELLOW}8. Paskolintų knygų sąrašas")
            print(f"{Fore.YELLOW}9. Grąžinti knygą")
            print(f"{Fore.BLACK}0. Baigti programą")
            

            choice = input(f"{Fore.GREEN}Pasirinkite ką norite atlikti: ")
            f"{Style.RESET_ALL}"

            if choice == '1':
                try:
                    title = input(f"{Fore.BLUE}Pavadinimas: ")
                    author = input("Autorius: ")
                    release = input("Išleidimo metai (YYYY): ")
                    genre = input("Žanras: ")
                    copies = int(input("Kopijų: "))
                    f"{Style.RESET_ALL}"
                    add_book(title, author, release, genre, copies)
                except KeyboardInterrupt as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")

            elif choice == '2':
                try:
                    year = int(input(f"{Fore.BLUE}Įveskite metus (pvz. 2000): "))
                    remove_books_older_than(year)
                    print(f"Knygos, senesnės nei {year}, buvo pašalintos. {Style.RESET_ALL}")
                except KeyboardInterrupt as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")

            elif choice == '3':
                try:
                    book_id = input(f"{Fore.BLUE}Įvesti knygos ID: ")
                    user = input(f"Jūsų vardas: ")
                    f"{Style.RESET_ALL}"
                    borrow_book(book_id, user)
                except KeyboardInterrupt as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")

            elif choice == '4':
                try:
                    title = input(f"{Fore.BLUE}Įvesti pavadinimą: ")
                    f"{Style.RESET_ALL}"
                    search_by_title(title)
                except KeyboardInterrupt as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")

            elif choice == '5':
                try:
                    author = input(f"{Fore.BLUE}Įvesti autorių: ")
                    f"{Style.RESET_ALL}"
                    search_by_author(author)
                except KeyboardInterrupt as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")

            elif choice == '6':
                try:
                    print(f"{Fore.BLUE}Knygų sąrašas: {Style.RESET_ALL}")
                    list_all_books()
                except KeyboardInterrupt as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")

            elif choice == '7':
                try:
                    print(f"{Fore.BLUE}Vėluojančių knygų sąrašas: {Style.RESET_ALL}")
                    list_overdue_books()
                except KeyboardInterrupt as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
            
            elif choice == '8':
                try:
                    print(f"{Fore.BLUE}Paskolintų knygų sąrašas: {Style.RESET_ALL}")
                    list_borrowed_books()
                except KeyboardInterrupt as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
            
            elif choice == '9':
                try:
                    book_id = input(f"{Fore.BLUE}Įveskite knygos ID: ")
                    user = input(f"Jūsų vardas: ")
                    f"{Style.RESET_ALL}"
                    return_book(book_id, user)
                except KeyboardInterrupt as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")

            elif choice == '0':
                print(f"{Fore.BLACK}Programa baigta.{Style.RESET_ALL}")
                break

            else:
                print("Blogas pasirinkimas, bandykite dar kartą.")
        except KeyboardInterrupt as e:
            print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Klaida, bandykite dar kartą. {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()