import uuid

class Book:
    def __init__(self, title, author, release_date, genre):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.release_date = release_date
        self.genre = genre

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Pavadinimas: {self.title}\n"
                f"Autorius: {self.author}\n"
                f"Išleidimo metai: {self.release_date}\n"
                f"Žanras: {self.genre}")