from utilities.save_load_data import load_data
from datetime import datetime

def check_overdue_books(user=None):
    books = load_data()
    overdue_books = []

    for book in books:
        for record in book.borrowed_by:
            try:
                due_date = datetime.strptime(record['due_date'], "%Y-%m-%d")
            except (KeyError, ValueError):
                continue

            if due_date < datetime.now():
                if user:
                    if record['user'] == user:
                        return True
                    continue
                overdue_books.append((book.title, record['user'], record['due_date']))

    if user:
        return False
    return overdue_books