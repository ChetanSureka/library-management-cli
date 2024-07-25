from hashlib import sha256 # sha256 encryption for password hashing
from datetime import datetime
import uuid

class User:
    '''
    User model for user data.
    - name: The name of the user
    - password
    '''
    def __init__(self, name: str, password: str):
        self.id = uuid.uuid4().int
        self.name = name
        self.password = self.hash_pass(password)
    
    def hash_pass(self, password: str):
        # hash the raw password into sha256 encoded
        return sha256(password.encode()).hexdigest()
    
    def to_dict(self):
        # return a user dictionary
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password
        }


class Book:
    '''
    Book model for books data
    - title: The title of the book
    - author: The author of the book
    - isbn: ISBN code of the book
    - qty: qty of the book
    '''
    def __init__(self, title: str, author: str, isbn: str, qty: int):
        self.id = uuid.uuid4().int
        self.title = title
        self.author = author
        self.isbn = isbn
        self.qty = qty
        self.date_added = datetime.now(tz='Asia/Kolkata').date()
    
    def to_dict(self):
        # return a book dictionary
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "qty": self.qty,
            "date_added": self.date_added
        }


class Transaction:
    '''
    Transaction model for book transactions
    - book_id: id of the book
    - user_id: user_id of the transaction
    - type: type of transaction (checkin/checkout)
    - qty: amount of books in the transaction
    '''
    def __init__(self, book_id: int, user_id: int, type: str, qty: int):
        self.id = uuid.uuid4().int
        self.book_id = book_id
        self.user_id = user_id
        self.type = type
        self.qty = qty
        self.date_added = datetime.now(tz='Asia/Kolkata').date()
    
    def to_dict(self):
        # return a transaction dictionary
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "type": self.type,
            "qty": self.qty,
            "date_added": self.date_added
        }

