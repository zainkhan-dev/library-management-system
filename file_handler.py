import json
import os

FILE_NAME = "library_data.json"


def save_books(book_list):

    data = [book.to_dict() for book in book_list]

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_books():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    from book import Book
    return [Book.from_dict(item) for item in data]