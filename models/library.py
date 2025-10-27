class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class LibraryModel:
    def __init__(self):
        # Pretend this is our small book database
        self.books = [
            Book("The Great Gatsby", "F. Scott Fitzgerald"),
            Book("To Kill a Mockingbird", "Harper Lee"),
            Book("1984", "George Orwell"),
            Book("Python Programming", "John Zelle"),
            Book("Fluent Python", "Luciano Ramalho")
        ]

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        return new_book
