import pickle
import os
import uuid

library_path = os.path.join(os.path.dirname(__file__), '../data/library.pickle')

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

def load_data():
    if not os.path.exists(library_path) or os.path.getsize(library_path) == 0:
        return []
    with open(library_path, 'rb') as f:
        return pickle.load(f)

def save_data(data):
    with open(library_path, 'wb') as f:
        pickle.dump(data, f)