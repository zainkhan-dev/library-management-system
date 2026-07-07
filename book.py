class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully.")
        else:
            print("Book already borrowed.")

    def return_book(self):
        self.available = True
        print("Book returned.")

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(data["title"], data["author"])
        book.available = data["available"]
        return book