# library_management.py

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Successfully checked out '{title}'.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Successfully returned '{title}'.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for title in available_books:
                print(f"   {title}")
        else:
            print("No books available in the library.")
