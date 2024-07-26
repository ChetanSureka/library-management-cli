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
        if book["qty"] == 0:
            print(f"Book '{book['title']}' not available for check out.")
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
        transactions = self.store.get_transactions()

        user = next((u for u in users if u["name"].lower() == user_name.lower()), None)
        book = next((b for b in books if b["isbn"] == isbn), None)
        
        if not user:
            print(f"User '{user_name}' not found.")
            return
        if not book:
            print(f"Book with ISBN '{isbn}' not found.")
            return
        
        # Calculate the total quantity of the book checked out and checked in by the user
        total_checked_out_qty = 0
        total_checked_in_qty = 0
        
        for t in transactions:
            if (t["user_id"] == user["id"]) and (t["book_id"] == book["id"]):
                if t["type"] == "check-in":
                    total_checked_in_qty += t["qty"]
                
                if t["type"] == "check-out":
                    total_checked_out_qty += t["qty"]
        
        if total_checked_in_qty + qty > total_checked_out_qty:
            print(f"User '{user_name}' trying to check in more books than checked out for book '{book['title']}' with ISBN '{isbn}'.")
            return
        
        book["qty"] += qty
        self.store._write_file(self.store.books_file, books)
        
        new_transaction = Transaction(book["id"], user["id"], "check-in", qty)
        self.store.add_transaction(new_transaction.to_dict())
        print(f"Book '{book['title']}' checked in successfully by '{user['name']}'.")

    def list_transactions(self):
        # List all transactions
        print("Listing all transactions")
        return self.store.get_transactions()

    def search_transactions(self, book_title=None, user_name=None, transaction_type=None):
        # search transactions by book title, user name, or transaction type
        transactions = self.store.get_transactions()
        users = self.store.get_users()
        books = self.store.get_books()

        if book_title:
            book = next((b for b in books if b["title"].lower() == book_title.lower()), None)
            if book:
                transactions = [t for t in transactions if t["book_id"] == book["id"]]
            else:
                print(f"Book '{book_title}' not found.")
                return []
        
        if user_name:
            user = next((u for u in users if u["name"].lower() == user_name.lower()), None)
            if user:
                transactions = [t for t in transactions if t["user_id"] == user["id"]]
            else:
                print(f"User '{user_name}' not found.")
                return []
        
        if transaction_type:
            transactions = [t for t in transactions if t["type"] == transaction_type]

        print(f"Transactions search results for book '{book_title}', user '{user_name}', type '{transaction_type}' retrieved successfully.")
        return transactions
