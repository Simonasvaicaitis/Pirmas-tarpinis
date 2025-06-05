from classes.book import load_data
from datetime import datetime

def check_overdue_books(user=None):
    books = load_data()
    overdue_books = []

    for book in books:
        for record in book.borrowed_by:
            due_date = datetime.strptime(record['due_date'], "%Y-%m-%d")
            if due_date < datetime.now():
                if user:
                    if record['user'] == user:
                        return True
                else:
                    overdue_books.append((book.title, record['user'], record['due_date']))

    if user:
        return False
    return overdue_books

def list_overdue_books():
    overdue = check_overdue_books()
    if overdue:
        print("Overdue Books:")
        for book_title, user, due_date in overdue:
            print(f"{book_title} – borrowed by {user}, due on {due_date}")
    else:
        print("Nėra vėluojančių knygų.")