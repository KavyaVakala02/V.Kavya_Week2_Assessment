class Book:   #main class
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __repr__(self):
        return f"'{self.title}' by {self.author}"
    # Overloading the '+' operator 
    def __add__(self, other):
        if isinstance(other, Book):
            return f"Series: {self.title} & {other.title}"
        return NotImplemented
book1 = Book("Book One", "Author A")
book2 = Book("Book Two", "Author B")
# Concatenate the two Book objects using overloaded '+' operator
print(book1 + book2)  
