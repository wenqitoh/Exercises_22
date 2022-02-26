"""design & build program for small local library
- books to be borrowed
- the users who will borrow the books
Wen-Qi Toh
24/2/22"""

class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title
        self.author = author
        self.dewey = dewey
        self.isbn = isbn
        self.available = True
        self.borrower = None
        book_list.append(self)  # holds book objects as created - main routine

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("###########################")


class User:
    def __init__(self, name, address):
        self.name = name    # string
        self.address = address  # string
        self.fees = 0.0  # float
        self.borrowed_books = []
        user_list.append(self)

    def user_details(self):
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Fees $", self.fees)
        print("###########################")


# print list of books
def print_info():
    for book in book_list:
        book.book_details()


# print list of users
def print_user():
    for user in user_list:
        user.user_details()


# add a new library user
def add_user():
    name = input("Enter the new user's name: ").title()
    address = input("Enter the new user's address: ")
    User(name, address)
    print(name, address,"has been added to the user list")


def add_book():
    title = input("Enter the new book's title: ").title()
    author = input("Enter the new book's author: ").title()
    dewey = input("Enter the new book's dewey code: ").upper()
    isbn = input("Enter the new book's ISBN: ")
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list")


def find_user():
    user_to_find = input("Enter the name of the user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return user
    print("Sorry, no user was found with that name")
    return None


# find a book
def find_book():
    book_to_find = input("Enter the name of the book: ").title()
    for book in book_list:
        if book.title == book_to_find:
            print(f"The book '{book_to_find}' is in the catalogue")
            return book
    print("Sorry, no book was found with that name")
    return None


def lend_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if book.available:
            confirm = input("Type 'Y' if you want to borrow this book: ").upper()
            if confirm == 'Y':
                print(f"Book title: '{book.title}' is now on loan to {user.name}")
                book.available = False  # set 'available' attribute
                book.borrower = user.name   # record borrower name
                user.borrowed_books.append(book.title)
        else:
            print(f"Sorry, '{book.title} is already out on loan")


def return_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if not book.available:
            confirm = input("Type 'Y' if you want to return this book: ").upper()
            if confirm == 'Y':
                print(f"Book title: '{book.title}' is now returned to the library")
                book.available = True
                book.borrower = user.name
                user.borrowed_books.remove(book.title)
        else:
            print(f"Sorry, '{book.title} is on loan to someone else")


# main routine
book_list = []
user_list = []

# create objects - books
Book("Lord of the Rings", "J.R.R.Tolkien", "TOL", "13345967573")
Book("The Hunger Games", "Suzanne Collins", "COL", "67459034982")
Book("A Tale of Two Cities", "Charles Dickens", "DIC", "573945823942")
Book("Harry Potter", "J.K.Rowling", "ROW", "349667549223")

# create objects - users
User("John", "34 Heeha flat")
User("Leticia", "12 Chicken St")
User("Lina", "15 Brownie St")
User("Aaron", "18 Blackford Rd")

# user menu
new_action = True
while new_action:
    print("1. Lend a book")
    print("2. Return a book")
    print("3. Add a user")
    print("4. Add a book")
    print("5. Exit")

    choice = input("\nWhat would you like to do? - enter a number: ")
    if choice == "1":
        lend_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        add_user()
    elif choice == "4":
        add_book()
    elif choice == "5":
        confirm = input("Type 'Y' if you want to exit the system - or any other"
                        " key to go back to the menu: ").upper()
        if confirm == "Y":
            print("Goodbye")
            new_action = False
    else:
        print("\n*** That was not a valid choice ***\n")
# printing the info
# add_book()
# print_info()
# find_user()
# find_book()
# lend_book()
# print("\n***********************************\n")
# return_book()

