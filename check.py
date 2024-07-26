from storage import StorageManager
from models import Transaction

class TransactionManager:
    '''
    Transaction manager class to handle check-in and check-out of books
    '''
    def __init__(self):
        self.store = StorageManager()
    
    def check_out_book(self, user_name, isbn, qty=1):
        # Check out a book by user name and book ISBN
        users = self.store.get_users()
        books = self.store.get_books()

        user = next((u for u in users if u["name"].lower() == user_name.lower()), None)
        book = next((b for b in books if b["isbn"] == isbn), None)
        
        if not user:
            print(f"User '{user_name}' not found.")
            return
        if not book:
            print(f"Book with ISBN '{isbn}' not found.")
            return
        if book["qty"] < qty:
            print(f"Not enough quantity of book '{book['title']}' available for check out.")
            return
        
        book["qty"] -= qty
        self.store._write_file(self.store.books_file, books)
        
        new_transaction = Transaction(book["id"], user["id"], "check-out", qty)
        self.store.add_transaction(new_transaction.to_dict())
        print(f"Book '{book['title']}' checked out successfully by '{user['name']}'.")

    def check_in_book(self, user_name, isbn, qty=1):
        # Check in a book by user name and book ISBN
        users = self.store.get_users()
        books = self.store.get_books()

        user = next((u for u in users if u["name"].lower() == user_name.lower()), None)
        book = next((b for b in books if b["isbn"] == isbn), None)
        
        if not user:
            print(f"User '{user_name}' not found.")
            return
        if not book:
            print(f"Book with ISBN '{isbn}' not found.")
            return
        
        book["qty"] += qty
        self.store._write_file(self.store.books_file, books)
        
        new_transaction = Transaction(book["id"], user["id"], "check-in", qty)
        self.store.add_transaction(new_transaction.to_dict())
        print(f"Book '{book['title']}' checked in successfully by '{user['name']}'.")

    def list_transactions(self):
        # List all transactions
        return self.store.get_transactions()

    def search_transactions(self, book_title=None, user_name=None, transaction_type=None):
        # search transactions by book title, user name, or transaction type
        transactions = self.store.get_transactions()
        users = self.store.get_users()
        books = self.store.get_books()

        if book_title:
            book_ids = [b["id"] for b in books if b["title"].lower() == book_title.lower()]
            transactions = [t for t in transactions if t["book_id"] in book_ids]
        
        if user_name:
            user_ids = [u["id"] for u in users if u["name"].lower() == user_name.lower()]
            transactions = [t for t in transactions if t["user_id"] in user_ids]
        
        if transaction_type:
            transactions = [t for t in transactions if t["type"].lower() == transaction_type.lower()]
        
        return transactions
