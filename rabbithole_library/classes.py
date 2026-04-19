from random import randint
from utils import sync as initialize, color_text as color_print
from datetime import datetime
from database import database

# The system imports:
# - randint: for generating unique IDs (users, publishers, books).
# - initialize (sync): to update and persist changes into the database.
# - color_print: for colored console outputs (visual feedback).
# - datetime: to track registration, borrowing, publishing, and return dates.
# - database: the main in-memory data storage for library entities.


# =========================
# User management
# =========================
class User:
    def __init__(self):
        pass

    def register(self, lib_id, fullname, email, phone):
        # Registers a new user into the library system
        # Automatically adds date of registration
        # Keeps track of borrowed books (IDs + full details separately)
        date_added = datetime.now()
        
        new_user = {
            "lib_id": str(lib_id),
            "fullname": fullname,
            "email": email,
            "phone": phone,
            "books_borrowed_ids": [],
            "books_borrowed": [],
            "date_added": date_added,
        }
        database[0]["data"]["users"].append(new_user)
        print(database[0]["data"]["users"])
        color_print(f"\nNew user added successfully. Libary id: {lib_id}", "green")

    def update(self, details, lib_id):
        # Updates user information: email and/or phone number
        # Uses flexible handling depending on fields present in 'details'
        if "email" in details and "phone" in details:
            for user in database[0]["data"]["users"]:
                if user["lib_id"] == lib_id:
                    user["phone"] = details["phone"]
                    user["email"] = details["email"]
                    initialize(database)
                    return
        elif "email" in details:
            # NOTE: This branch uses database["users"], possibly inconsistent with above (might be a unique quirk/bug).
            for user in database["users"]:
                if user["lib_id"] == lib_id:
                    user["email"] = details["email"]
                    initialize(database)
                    return
        elif "phone" in details:
            for user in database[0]["data"]["users"]:
                if user["lib_id"] == lib_id:
                    user["phone"] = details["phone"]
                    initialize(database)
                    return

    def remove(self, lib_id):
        # Removes a user by library ID
        # Uses `del user` which may not fully remove from list (unique handling worth noting).
        for user in database[0]["data"]["users"]:
            if user["lib_id"] == lib_id:
                del user
                initialize(database)
                return

    def login(self, id_, psw):
        # Authenticates staff (not normal users) using ID and password
        for staff in database[0]["data"]["staffs"]:
            if staff["id"] == id_ and staff["psw"] == psw:
                return staff
        return False

    def get_user(self, user_id):
        # Retrieves full user details by library ID
        for user in database[0]["data"]["users"]:
            if user["lib_id"] == user_id:
                return user
        


# =========================
# Publisher management
# =========================
class Publisher:
    def __init__(self):
        pass

    def add(self, name, year_established):
        # Adds a publisher with random unique ID
        id_ = randint(121000, 121999)
        new_publisher = {
            "id": str(id_),
            "name": name,
            "year_established": year_established,
        }
        database[0]["data"]["publishers"].append(new_publisher)
        return new_publisher

    def get(self, id_):
        # Retrieves publisher details by ID
        for publisher in database[0]["data"]["publishers"]:
            if publisher["id"] == id_:
                initialize(database)  # sync after read (unique: not common practice)
                return publisher
        return


# =========================
# Book management
# =========================
class Book:
    def __init__(self):
        self.publisher = Publisher()

    def add(
        self,
        title,
        author_firstname,
        author_title,
        author_lastname,
        publisher_id,
        serial_num,
        genre,
        year_published,
    ):
        # Adds a book into the library
        # Includes publisher details for easy cross-referencing
        publisher_details = self.publisher.get(publisher_id)
        id_ = randint(191000, 191999)
        date_added = datetime.now()
        new_book = {
            "id": id_,
            "date_added": date_added,
            "title": title,
            "author_firstname": author_firstname,
            "author_title": author_title,
            "author_lastname": author_lastname,
            "publisher_id": publisher_id,
            "year_published": year_published,
            "serial_num": serial_num,
            "genre": genre,
            "publisher_details": publisher_details,
        }
        database[0]["data"]["books"].append(new_book)

        color_print(f"\nBook: {title} added successfully!", "green")

    def remove(self, id_):
        # Deletes a book by ID
        for book in database[0]["data"]["books"]:
            if book["id"] == id_:
                database[0]["data"]["books"].remove(book)
                print("\nBook Deleted Successfully!\n")
                return
        print("Book not found!")

    def all(self):
        # Returns list of all books in the system
        result = []
        for book in database[0]["data"]["books"]:
            result.append(book)
        return result

    # Search methods (by different attributes)
    def in_title(self, text):
        result = []
        for book in database[0]["data"]["books"]:
            if text.lower() in book["title"].lower():
                result.append(book)
        return result

    def in_author_name(self, text):
        result = []
        for book in database[0]["data"]["books"]:
            if (
                text.lower()
                in book["author_firstname"].lower()
                + " "
                + book["author_lastname"].lower()
            ):
                result.append(book)
        return result

    def in_publisher(self, text):
        result = []
        for book in database[0]["data"]["books"]:
            if text.lower() in book["publisher_details"]["name"].lower():
                result.append(book)
        return result

    def in_genre(self, text):
        result = []
        for book in database[0]["data"]["books"]:
            if text.lower() in book["genre"].lower():
                result.append(book)
        return result

    def in_year(self, text):
        result = []
        for book in database[0]["data"]["books"]:
            if text.lower() in book["year_published"].lower():
                result.append(book)
        return result

    def get(self, book_id):
        # Retrieves a single book by ID
        data = None
        for book in database[0]["data"]["books"]:
            if book["id"] == book_id:
                data = book
                return data

    def title(self, book_id):
        # Retrieves only the title of a book by ID
        for book in database[0]["data"]["books"]:
            if book["id"] == book_id:
                return book["title"]


# =========================
# Borrowing management
# =========================
class BookBorrow(Book):
    def __init__(self):
        pass

    def do_borrow(self, user_id, book_id, due_date):
        # Handles borrowing of a book by a user
        date_borrowed = datetime.now()
        new_book_borrow = {
            "lib_id": user_id,
            "book_id": book_id,
            "date_borrowed": date_borrowed,
            "due_date": due_date,
        }
        database[0]["data"]["books_borrowed"].append(new_book_borrow)
        title = self.title(book_id)
        to_print = f"The Book {title} has been successfully borrowed for the user with lab id: {user_id} to be returned on {due_date}."

        # Update user borrow history (both IDs and book objects stored separately — unique design choice)
        for user in database[0]["data"]["users"]:
            if user["lib_id"] == user_id:
                user["books_borrowed"].append(self.get(book_id))
                user["books_borrowed_ids"].append(book_id)

        color_print(to_print, "green")

    def do_return(self, user_id, book_id):
        # Handles returning of a borrowed book
        for book in database[0]["data"]["books_borrowed"]:
            if book["lib_id"] == user_id and book["book_id"] == book_id:
                database[0]["data"]["books_borrowed"].remove(book)

        for user in database[0]["data"]["users"]:
            if user["lib_id"] == user_id:
                for book in user["books_borrowed"]:
                    # NOTE: This compares full book object vs ID (quirk, might cause logical mismatch).
                    if book == book_id:
                        user["books_borrowed"].remove(book)

        color_print("Book Returned Successfully", "green")


# =========================
# Staff (Admin functionality)
# =========================
class Staff(User):
    def __init__(self):
        self.book = Book()
        self.user = User()
        self.book_borrow = BookBorrow()

    def delete_book(self, id_, psw, book_id):
        # Staff-authenticated book deletion
        for staff in database[0]["data"]["staffs"]:
            if staff["id"] == id_ and staff["psw"] == psw:
                self.book.remove(book_id)

    def new_book(
        self,
        title,
        author_firstname,
        author_title,
        author_lastname,
        publisher_id,
        serial_num,
        genre,
        year_published,
    ):
        # Staff-authenticated book creation
        self.book.add(
            title,
            author_firstname,
            author_title,
            author_lastname,
            publisher_id,
            serial_num,
            genre,
            year_published,
        )

    def add_user(self, id_, psw, fullname, email, phone):
        # Staff-authenticated user registration
        for staff in database[0]["data"]["staffs"]:
            if staff["id"] == id_ and staff["psw"] == psw:
                lib_id = randint(151000, 151999)
                self.user.register(lib_id, fullname, email, phone)

    def view_user(self, id_, psw, user_id):
        # Staff-authenticated user profile + borrow history view
        for staff in database[0]["data"]["staffs"]:
            if staff["id"] == id_ and staff["psw"] == psw:
                user = self.user.get_user(user_id)
                if user != "none" and user != None:
                    print(user)
                    color_print(
                        f"\nID: {user['lib_id']} | Name: {user['fullname']} | Email: {user['email']} | Date Registered: {user['date_added']} | Phone: {user['phone']} "
                    ,"green")
                    print("\nBORROW HISTORY:")
                    # Show borrowed book details
                    for i_d in user["books_borrowed_ids"]:
                        for book in database[0]["data"]["books"]:
                            if book["id"] == i_d:
                                details = f"\nID: {book['id']}, Title: {book['title']}, Author: {book['author_title']} {book['author_firstname']} {book['author_lastname']}, Publisher: {book['publisher_details']['name']}, Year Published: {book['year_published']}, Serial Number: {book['serial_num']}, Genre: {book['genre']}"
                                print(details)

                                # Check if returned or not
                                print("\nRETURN STATUS:")
                                is_returned = None
                                for bb in database[0]["data"]["books_borrowed"]:
                                    if (
                                        bb["lib_id"] == user_id
                                        and bb["book_id"] == book["id"]
                                    ):
                                        color_print(
                                            f"Not returned. Due Date: {bb['due_date']} | Borrow Date: {bb['date_borrowed']}",
                                            "red",
                                        )
                                        is_returned = False
                                if is_returned != False:
                                    color_print("Returned", "green")
                else:
                    color_print("User Not Found","red")

    def borrow_book(self, id_, psw, user_id, book_id, due_date):
        # Staff-authenticated borrow operation
        for staff in database[0]["data"]["staffs"]:
            if staff["id"] == id_ and staff["psw"] == psw:
                self.book_borrow.do_borrow(user_id, book_id, due_date)

    def return_book(self, id_, psw, user_id, book_id):
        # Staff-authenticated return operation
        for staff in database[0]["data"]["staffs"]:
            if staff["id"] == id_ and staff["psw"] == psw:
                self.book_borrow.do_return(user_id, book_id)

    def search(self, id_, psw, search_type, text):
        # Staff-authenticated multi-criteria search
        # Search can be by: title, author_name, publisher, genre, year
        for staff in database[0]["data"]["staffs"]:
            if staff["id"] == id_ and staff["psw"] == psw:
                if search_type == "title":
                    result = self.book.in_title(text)
                    for book in result:
                        details = f"\nID: {book['id']}, Title: {book['title']}, Author: {book['author_title']} {book['author_firstname']} {book['author_lastname']}, Publisher: {book['publisher_details']['name']}, Year Published: {book['year_published']}, Serial Number: {book['serial_num']}, Genre: {book['genre']}"
                        print(details)

                elif search_type == "author_name":
                    result = self.book.in_author_name(text)
                    for book in result:
                        details = f"\nID: {book['id']}, Title: {book['title']}, Author: {book['author_title']} {book['author_firstname']} {book['author_lastname']}, Publisher: {book['publisher_details']['name']}, Year Published: {book['year_published']}, Serial Number: {book['serial_num']}, Genre: {book['genre']}"
                        print(details)
                elif search_type == "publisher":
                    result = self.book.in_publisher(text)
                    for book in result:
                        details = f"\nID: {book['id']}, Title: {book['title']}, Author: {book['author_title']} {book['author_firstname']} {book['author_lastname']}, Publisher: {book['publisher_details']['name']}, Year Published: {book['year_published']}, Serial Number: {book['serial_num']}, Genre: {book['genre']}"
                        print(details)
                elif search_type == "genre":
                    result = self.book.in_genre(text)
                    for book in result:
                        details = f"\nID: {book['id']}, Title: {book['title']}, Author: {book['author_title']} {book['author_firstname']} {book['author_lastname']}, Publisher: {book['publisher_details']['name']}, Year Published: {book['year_published']}, Serial Number: {book['serial_num']}, Genre: {book['genre']}"
                        print(details)
                elif search_type == "year":
                    result = self.book.in_year(text)
                    for book in result:
                        details = f"\nID: {book['id']}, Title: {book['title']}, Author: {book['author_title']} {book['author_firstname']} {book['author_lastname']}, Publisher: {book['publisher_details']['name']}, Year Published: {book['year_published']}, Serial Number: {book['serial_num']}, Genre: {book['genre']}"
                        print(details)
