# Library Management System

## Overview

This Library Management System is designed to manage book check-ins and check-outs, as well as user and book information. The system supports adding, updating, and deleting users and books, and keeps track of all transactions. The project includes logging capabilities to track operations and errors.

## Features

- **User Management**
  - Add, update, delete, and list users.
  - Search users by ID or name.

- **Book Management**
  - Add, update, delete, and list books.
  - Search books by title or ISBN.

- **Transaction Management**
  - Check-out and check-in books.
  - Ensure users cannot check in more books than they have checked out.
  - List and search transactions.

- **Logging**
  - Logs operations and errors to `storage.log`.

## Project Structure

- `main.py`: Main application file to handle user interface.
- `storage.py`: Handles data storage witin json file.
- `models.py`: Contains data models for `User`, `Book`, and `Transaction`.
- `user.py`: Manages user-related operations.
- `book.py`: Manages book-related operations.
- `storage.log`: Log file for storage operations.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ChetanSureka/library-management-cli.git
   cd library-management-cli

2. Running the application:
    ```bash
    python main.py
## Screenshots
Below are the Screenshots for the Main menu, Books listing and Search Books

### Main menu
![image](https://github.com/user-attachments/assets/e651fbba-5872-4983-8fc0-aa9b035ad23a)

### List Books
![screenshot](https://github.com/user-attachments/assets/8f78d6c9-71a4-4bc3-9fe8-c3334640a862)

### Search Books
![image](https://github.com/user-attachments/assets/fcf1b92f-83f5-42a3-9d32-ec60f6bd616c)

## Authors

- [@ChetanSureka](https://www.github.com/ChetanSureka)


## Feedback

If you have any feedback, please reach me out at surekachetan09@gmail.com

