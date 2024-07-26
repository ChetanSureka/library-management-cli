import sys
from user import UserManager
from book import BookManager
from check import TransactionManager

def main_menu():
    print("\nLibrary Management System")
    print("1. Add User")
    print("2. List Users")
    print("3. Search Users")
    print("4. Delete User")
    print("5. Update User")
    print("6. Add Book")
    print("7. List Books")
    print("8. Search Books")
    print("9. Delete Book")
    print("10. Update Book")
    print("11. Check Out Book")
    print("12. Check In Book")
    print("13. List Transactions")
    print("14. Search Transactions")
    print("0. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    user_manager = UserManager()
    book_manager = BookManager()
    transaction_manager = TransactionManager()

    while True:
        choice = main_menu()
        if choice == '1':
            name = input("Enter user name: ").lower()
            password = input("Enter user password: ")
            user_manager.add_user(name, password)
        
        elif choice == '2':
            users = user_manager.list_users()
            for user in users:
                print(user)
        
        elif choice == '3':
            user_input = input("Search user by name: ").lower()
            users = user_manager.search_user(name=user_input)
            for user in users:
                print(user)
        
        elif choice == '4':
            user_input = input("Delete user by name: ").lower()
            users = user_manager.search_user(name=user_input)
            if users:
                user_manager.delete_user(user_input)
            else:
                print(f"User with name '{user_input}' not found.")
        
        elif choice == '5':
            user_input = input("Update user by name: ").lower()
            users = user_manager.search_user(name=user_input)
            if users:
                new_name = input("Enter new name (leave blank to keep current name): ").lower()
                new_password = input("Enter new password (leave blank to keep current password): ")
                if new_name == '':
                    new_name = None
                if new_password == '':
                    new_password = None
                user_manager.update_user(user_input, new_name, new_password)
            else:
                print(f"User with name '{user_input}' not found.")
        
        elif choice == '6':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            qty = int(input("Enter book quantity: "))
            book_manager.add_book(title, author, isbn, qty)
        
        elif choice == '7':
            books = book_manager.list_books()
            for book in books:
                print(book)
        
        elif choice == '8':
            search_by = input("Search book by ISBN, title, or author? ").lower()
            if search_by == 'isbn':
                isbn = input("Enter book ISBN: ")
                books = book_manager.search_books(isbn=isbn)
            elif search_by == 'title':
                title = input("Enter book title: ").lower()
                books = book_manager.search_books(title=title)
            elif search_by == 'author':
                author = input("Enter book author: ").lower()
                books = book_manager.search_books(author=author)
            else:
                print("Invalid search criteria.")
                continue
            for book in books:
                print(book)
        
        elif choice == '9':
            isbn = input("Delete book by ISBN: ")
            books = book_manager.search_books(isbn=isbn)
            if books:
                book_manager.delete_book(isbn)
            else:
                print(f"Book with ISBN '{isbn}' not found.")
        
        elif choice == '10':
            isbn = input("Update book by ISBN: ")
            books = book_manager.search_books(isbn=isbn)
            if books:
                new_title = input("Enter new title (leave blank to keep current title): ")
                new_author = input("Enter new author (leave blank to keep current author): ")
                new_qty = input("Enter new quantity (leave blank to keep current quantity): ")
                if new_title == '':
                    new_title = None
                if new_author == '':
                    new_author = None
                if new_qty == '':
                    new_qty = None
                else:
                    new_qty = int(new_qty)
                book_manager.update_book(isbn, new_title, new_author, new_qty)
            else:
                print(f"Book with ISBN '{isbn}' not found.")
        
        elif choice == '11':
            user_name = input("Enter user name: ").lower()
            isbn = input("Enter book ISBN: ")
            qty = int(input("Enter quantity to check out: "))
            transaction_manager.check_out_book(user_name, isbn, qty)
        
        elif choice == '12':
            user_name = input("Enter user name: ").lower()
            isbn = input("Enter book ISBN: ")
            qty = int(input("Enter quantity to check in: "))
            transaction_manager.check_in_book(user_name, isbn, qty)
        
        elif choice == '13':
            transactions = transaction_manager.list_transactions()
            for transaction in transactions:
                print(transaction)
        
        elif choice == '14':
            search_by = input("Search transactions by book title, user name, or type? ").lower()
            if search_by == 'title':
                book_title = input("Enter book title: ").lower()
                transactions = transaction_manager.search_transactions(book_title=book_title)
            elif search_by == 'user name':
                user_name = input("Enter user name: ").lower()
                transactions = transaction_manager.search_transactions(user_name=user_name)
            elif search_by == 'type':
                transaction_type = input("Enter transaction type (check-in/check-out): ").lower()
                transactions = transaction_manager.search_transactions(transaction_type=transaction_type)
            else:
                print("Invalid search criteria.")
                continue
            for transaction in transactions:
                print(transaction)
        
        elif choice == '0':
            print("Exiting.")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
