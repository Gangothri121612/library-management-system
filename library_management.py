class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Available: {'Yes' if self.is_available else 'No'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully:", book.title)

    def remove_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print("Book removed successfully:", book.title)
                return
        print("Book with ID", book_id, "not found.")

    def search_book(self, title):
        found = False
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
                found = True
        if not found:
            print("No books found with title containing:", title)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library Books:")
            for book in self.books:
                print(book)

    def borrow_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                if book.is_available:
                    book.is_available = False
                    print("Book borrowed successfully:", book.title)
                else:
                    print("Book is already borrowed:", book.title)
                return
        print("Book with ID", book_id, "not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully:", book.title)
                else:
                    print("Book is already available:", book.title)
                return
        print("Book with ID", book_id, "not found.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            library.add_book(Book(book_id, title, author))

        elif choice == 2:
            library.remove_book(input("Enter Book ID to remove: "))

        elif choice == 3:
            library.search_book(input("Enter Book Title to search: "))

        elif choice == 4:
            library.display_books()

        elif choice == 5:
            library.borrow_book(input("Enter Book ID to borrow: "))

        elif choice == 6:
            library.return_book(input("Enter Book ID to return: "))

        elif choice == 7:
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
