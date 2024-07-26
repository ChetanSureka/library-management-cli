import os
import json
import logging

user_file = 'storage/user.json'
books_file = 'storage/books.json'
transactions_file = 'storage/transactions.json'

# Configure logging
logging.basicConfig(filename='storage.log',
                    level=logging.INFO,
                    format='[%(levelname)s] [%(funcName)s] [%(asctime)s] [%(message)s]',
                    datefmt='%Y-%m-%d %H:%M:%S')

class StorageManager:
    '''
    Storage class that handles the storage operations (read, write)
        - user_file         : stores user data
        - books_file        : stores book data
        - transactions_file : stores transaction data
    '''
    def __init__(self,
                user_file=user_file,
                books_file=books_file,
                transactions_file=transactions_file):
        
        self.user_file = user_file
        self.books_file = books_file
        self.transactions_file = transactions_file
        
        # ensure the files exist
        self._file_exists(self.user_file)
        self._file_exists(self.books_file)
        self._file_exists(self.transactions_file)
    
    
    # Helper methods
    
    def _file_exists(self, path):
        # checks if the file exists, if not creates a new one
        if not os.path.exists(path):
            with open(path, 'w') as f:
                json.dump([], f)
            logging.info(f"Created file: {path}")
        
    def _read_file(self, path):
        # read file contents
        with open(path, 'r') as f:
            data = json.load(f)
        logging.info(f"Read data from file: {path}")
        return data
    
    def _write_file(self, path, data):
        # write the data to file
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"Written data to file: {path}")
    
    # Read, write user data to file
    
    def add_user(self, user_data):
        users = self._read_file(self.user_file)
        users.append(user_data)
        self._write_file(self.user_file, users)
        logging.info(f"Added user data: {user_data}")
    
    def get_users(self):
        return self._read_file(self.user_file)


    # Read, write book data to file

    def add_book(self, book_data):
        books = self._read_file(self.books_file)
        books.append(book_data)
        self._write_file(self.books_file, books)
        logging.info(f"Added book data: {book_data}")

    def get_books(self):
        return self._read_file(self.books_file)

    
    # Read, write transaction data to file
    
    def add_transaction(self, transaction_data):
        transactions = self._read_file(self.transactions_file)
        transactions.append(transaction_data)
        self._write_file(self.transactions_file, transactions)
        logging.info(f"Added transaction data: {transaction_data}")

    def get_transactions(self):
        return self._read_file(self.transactions_file)
