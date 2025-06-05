import pickle
import os

def library_path():
    return os.path.join(os.path.dirname(__file__), '../data/library.pickle')


def load_data():
    path = library_path()
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return []
    with open(path, 'rb') as f:
        return pickle.load(f)

def save_data(data):
    path = library_path()
    with open(path, 'wb') as f:
        pickle.dump(data, f)