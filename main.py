from library import Library
from file_handler import save_books, load_books


library = Library()

library.books = load_books()


while True:

    print("\n Library Management System")
    print("1.Add Book")
    print("2.Delete Book")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5.Search Book")
    print("6.Show Books")
    print("7.Save & Exit")

    try:

        choice = int(input("Choice: "))

        if choice == 1:

            title = input("Title: ")
            author = input("Author: ")

            library.add_book(title, author)

        elif choice == 2:

            title = input("Title: ")

            library.delete_book(title)

        elif choice == 3:

            title = input("Title: ")

            library.borrow_book(title)

        elif choice == 4:

            title = input("Title: ")

            library.return_book(title)

        elif choice == 5:

            title = input("Search: ")

            library.search_book(title)

        elif choice == 6:

            library.show_books()

        elif choice == 7:

            save_books(library.books)

            print("Saved!")

            break

        else:

            print("Invalid option.")

    except ValueError:

        print("Please enter a number.")

    except Exception as e:

        print("Unexpected Error:", e)