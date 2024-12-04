class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Initially, the book is not borrowed
    
    def mark_as_borrowed(self):
        """Marks the book as borrowed."""
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been marked as borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")
    
    def mark_as_returned(self):
        """Marks the book as returned."""
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List to store borrowed books
    
    def borrow_book(self, book):
        """Allows the member to borrow a book if it is available."""
        if not book.is_borrowed:
            book.mark_as_borrowed()  # Mark the book as borrowed
            self.borrowed_books.append(book)  # Add the book to borrowed list
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is already borrowed.")
    
    def return_book(self, book):
        """Allows the member to return a borrowed book."""
        if book in self.borrowed_books:
            book.mark_as_returned()  # Mark the book as returned
            self.borrowed_books.remove(book)  # Remove the book from borrowed list
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} cannot return '{book.title}' because it wasn't borrowed.")
    
    def list_borrowed_books(self):
        """Lists all borrowed books."""
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")