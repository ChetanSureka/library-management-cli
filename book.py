from storage import StorageManager
from models import Book

class BookManager:
    '''
    Book manager class to handle book management
    '''
    def __init__(self):
        self.store = StorageManager()
    
    
    def list_books(self):
        # List all books
        return self.store.get_books()
    
    
    def search_books(self, isbn=None, title=None, author=None):
        # search books by ISBN, title, or author
        books = self.store.get_books()
        
        if isbn:
            return [book for book in books if book["isbn"] == isbn]
        elif title:
            return [book for book in books if book["title"].lower() == title.lower()]
        elif author:
            return [book for book in books if book["author"].lower() == author.lower()]
        else:
            return []
    
    
    
    def add_book(self, title, author, isbn, qty):
        # add book to the list
        
        books = self.store.get_books()
        
        for book in books:
            if book["isbn"] == isbn:
                print(f"Book with ISBN {isbn} already exists.")
                return
        
        new_book = Book(title, author, isbn, qty)
        self.store.add_book(new_book.to_dict())
        print(f"Book {title} added successfully.")

    
    
    def update_book(self, isbn, new_title=None, new_author=None, new_qty=None):
        # update book details
        
        books = self.store.get_books()
        for book in books:
            if book["isbn"] == isbn:
                if new_title is not None and new_title != book["title"]:
                    book["title"] = new_title
                if new_author is not None and new_author != book["author"]:
                    book["author"] = new_author
                if new_qty is not None:
                    book["qty"] = new_qty
                
                self.store._write_file(self.store.books_file, books)
                print(f"Updated book with ISBN {isbn} successfully.")
                return 
        print(f"Book with ISBN {isbn} not found.")
        return
    
    
    
    def delete_book(self, isbn):
        # delete book by ISBN
        
        books = self.store.get_books()
        updated_books = [book for book in books if book['isbn'] != isbn]
        
        if len(updated_books) != len(books):
            self.store._write_file(self.store.books_file, updated_books)
            print(f"Book with ISBN {isbn} deleted.")
        else:
            print(f"Book with ISBN {isbn} not found.")
        return
