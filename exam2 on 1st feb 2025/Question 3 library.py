class Book:
    def __init__(self, title, author, isbn):  #parameterized constructor
        self.title = title
        self.author = author
        self.isbn = isbn
    def display_details(self):      #method to display details of the book
        print("\nBook Details:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
book1 = Book("The Book", "Author name", "1234567890")  #creating object
book1.display_details()
