class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n--- Library Books ---")

        for book in self.books:
            status = "Available" if book.available else "Issued"

            print(
                f"ID: {book.book_id} | "
                f"Title: {book.title} | "
                f"Author: {book.author} | "
                f"Status: {status}"
            )

    def search_book(self):
        title = input("Enter book title to search: ")

        found = False

        for book in self.books:
            if title.lower() in book.title.lower():
                print(
                    f"Found: {book.title} by {book.author}"
                )
                found = True

        if not found:
            print("Book not found.")

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                print("Book issued successfully!")
                return

        print("Book unavailable.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print("Book returned successfully!")
                return

        print("Book not found.")

    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")

        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book deleted successfully!")
                return

        print("Book not found.")


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice.")
