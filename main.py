import sys
from user import UserManager

def main_menu():
    print("\nLibrary Management System")
    print("1. Add User")
    print("2. List Users")
    print("3. Search Users")
    print("4. Delete User")
    print("5. Update User")
    print("0. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    user_manager = UserManager()

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
        
        elif choice == '0':
            print("Exiting.")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
