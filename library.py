from book import Book


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):

        self.books.append(Book(title, author))

        print("Book added.")

    def delete_book(self, title):

        for book in self.books:

            if book.title.lower() == title.lower():

                self.books.remove(book)
                print("Deleted.")
                return

        print("Book not found.")

    def search_book(self, title):

        for book in self.books:

            if title.lower() in book.title.lower():

                status = "Available" if book.available else "Borrowed"

                print(book.title, "-", book.author, "-", status)

                return

        print("Book not found.")

    def borrow_book(self, title):

        for book in self.books:

            if book.title.lower() == title.lower():

                book.borrow()
                return

        print("Book not found.")

    def return_book(self, title):

        for book in self.books:

            if book.title.lower() == title.lower():

                book.return_book()
                return

        print("Book not found.")

    def show_books(self):

        if len(self.books) == 0:
            print("No books.")

        for book in self.books:

            status = "Available" if book.available else "Borrowed"

            print(f"{book.title} | {book.author} | {status}")