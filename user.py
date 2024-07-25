from storage import StorageManager
from models import User

class UserManager:
    '''
    User manager class to handle user
    '''
    def __init__(self):
        self.store = StorageManager()
    
    def list_users(self):
        # List all users
        return self.store.get_users()
    
    def search_user(self, id=None, name=None):
        # search user by name / id
        users = self.store.get_users()
        
        if id:
            # matching_users = []
            # for user in users:
            #     if user['id'] == id:
            #         matching_users.append(user)
            return [user for user in users if user["id"] == id]
        elif name:
            return [user for user in users if user["name"] == name]
        else:
            return []
    
    
    def add_user(self, name, password):
        # add user to the list
        
        users = self.store.get_users()
        
        for user in users:
            if user["name"] == name:
                print(f"User with name {name} already exists.")
                return
        
        new_user = User(name, password)
        self.store.add_user(new_user.to_dict())
        print(f"User {name} added successfully.")


    def update_user(self, name, new_name=None, new_password=None):
        # update user to the list with the updated name/password
        
        users = self.store.get_users()
        for user in users:
            if user["name"] == name:
                if new_name is not None and new_name != user["name"]:
                    user["name"] = new_name
                if new_password is not None:
                    user["password"] = User.hash_pass(User, new_password)
                
                self.store._write_file(self.store.user_file, users)
                print(f"Updated user {name} successfully.")
                return 
        print(f"User with name {name} not found.")
        return
    
    def delete_user(self, name):
        # delete user by user name
        
        users = self.store.get_users()
        updated_users = [user for user in users if user['name'] != name]
        
        if len(updated_users) != len(users):
            self.store._write_file(self.store.user_file, updated_users)
            print(f"User with name {name} deleted.")
        else:
            print(f"User with name {name} not found.")
        return
    
    