import random

class Book:
    def __init__(self, title, author, bid):
        self.title = title
        self.author = author
        self.bid = bid


class LibraryModel:
    def __init__(self):
        # Pretend this is our small book database
        self.books = []
        self.bid_list = []

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def search_by_bid(self, bid):
        return [book for book in self.books if bid in book.bid]
    
    def add_book(self, title, author):
        while(1):
            try_bid=str(random.randint(1,10000))
            if try_bid not in self.bid_list:
                self.bid_list.append(try_bid)
                break
        new_book = Book(title,author,try_bid)
        self.books.append(new_book)
        return new_book
    
    def delete_book(self,bid):
        for index, book in enumerate(self.books):
            if book.bid==bid:
                self.bid_list.pop(index)
                return self.books.pop(index)
        return False

    def adjust_content(self, new_title, new_author, bid):
        for index, book in enumerate(self.books):
            if book.bid==bid:
                new_book=Book(new_title, new_author, bid)
                self.books[index]=new_book
                return new_book
        return False
        
        
