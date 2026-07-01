class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display_info(self):
        print(f"The title of the book is {self.title}")
        print(f"The author of the book is {self.author}")
        if self.available:
            print(f"The book is in the library.")
        else:
            print("The book is not in the library.")


    def checkout(self):
        if self.available:
            print(f"{self.title} The book is borrowed from the library.")
            self.available = False
        else:
            print(f"{self.title} The book not in the library.")

    def checkin(self):
        if not self.available:
            print(f"{self.title} the book has been returned to the library.")
            self.available = True
        else:
            print(f"{self.title} The book has not been returned to the library.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def display_books(self):
        print("Library books: ")
        for book in self.books:
            book.display_info()

book1 = Book("Hamlet", "Shakespeare")
book2 = Book("The silent Patient", "Alex M.")
book3 = Book("1984", "George Orwell")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


library.display_books()

book2.checkout()

library.display_books()

book2.checkin()

library.display_books()



