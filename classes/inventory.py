from classes.book import Book

class Inventory(Book):
    def __init__(self, title, author, release_date, genre, total_copies):
        super().__init__(title, author, release_date, genre)
        self.total_copies = total_copies
        self.borrowed_by = []