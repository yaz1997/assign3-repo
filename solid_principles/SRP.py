class Book:
    def __init__(self, title, author, isbn, genre, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability

    def __str__(self):
        availability_status = "Available" if self.availability else "Not Available"
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nGenre: {self.genre}\nAvailability: {availability_status}\n"


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book_details(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def get_all_books(self):
        return self.books


class BookBorrowingSystem:
    def __init__(self):
        self.borrowed_books = set()

    def borrow_book(self, book):
        if book.availability:
            book.availability = False
            self.borrowed_books.add(book)
            print(f"Book '{book.title}' has been borrowed.")
        else:
            print(f"Book '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.availability = True
            self.borrowed_books.remove(book)
            print(f"Book '{book.title}' has been returned.")
        else:
            print(f"Book '{book.title}' is not borrowed or already returned.")

    def borrowed_books_list(self):
        return list(self.borrowed_books)


if __name__ == "__main__":
    library = LibraryCatalog()
    borrowing_system = BookBorrowingSystem()

    # Adding books to the library catalog
    book1 = Book("Book1", "Author1", "ISBN1", "Fiction")
    book2 = Book("Book2", "Author2", "ISBN2", "Thriller")
    book3 = Book("Book3", "Author3", "ISBN3", "Mystery")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Borrowing and returning books
    borrowing_system.borrow_book(book1)
    borrowing_system.borrow_book(book2)
    borrowing_system.borrow_book(book2)  # Trying to borrow the same book again
    borrowing_system.return_book(book3)
    borrowing_system.return_book(book1)
    borrowing_system.return_book(book3)  # Trying to return the same book again

    # Get all borrowed books
    borrowed_books = borrowing_system.borrowed_books_list()
    print("\nBorrowed Books:")
    for book in borrowed_books:
        print(book)

