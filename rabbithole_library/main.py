import classes
import pyfiglet
from utils import color_text as color_print
from database import database

# Extract publishers from the database for quick reference when adding books
pubs = database[0]["data"]["publishers"]
pub_details = []
for a in pubs:
    pub_details.append(f"Name: {a['name']}| ID: {a['id']}")

# ASCII art logo for branding / aesthetics
logo = pyfiglet.figlet_format("RABBIT HOLE")

# Authentication placeholders
auth_staff = None
authenticated = False


def menu():
    """
    Displays the main menu options to authenticated staff.
    Menu contains core library operations:
    - View/Add/Delete books
    - Add users
    - Search books
    - Borrow/Return books
    - View users
    - Exit
    """
    color_print(
        f"\nHowdy {auth_staff['fullname']}, What would you like to do?\n", "green"
    )
    options = (
        "1. View Books\n2. Add New Book\n3. Delete Book\n4. Add New Libary User\n"
        "5. Search Books\n6. Borrow A Book For A User\n7. Return A Book For A User\n"
        "8. View User By ID\n9. Exit"
    )
    color_print(options, "green")


def authenticate():
    """
    Authenticates staff using ID and password.
    - Creates a Staff instance
    - Prompts for login credentials
    - If correct -> sets global auth variables and calls start()
    - If incorrect -> re-prompts recursively
    """
    staff = classes.Staff()
    color_print("\nPlease sign in as staff bellow:", "green")
    id_ = input("ID:>>>")
    psw = input("Password:>>>")
    if staff.login(id_, psw) != False:
        global auth_staff, authenticated
        auth_staff = staff.login(id_, psw)  # store authenticated staff object
        authenticated = True
        start()
        pass
    else:
        color_print("Incorrect id or password, pls try again!", "red")
        authenticate()  # recursion ensures re-attempt


def start():
    """
    Main entry point for the library system.
    - Prints logo and welcome message
    - Runs authentication if not logged in
    - Initializes Book, Staff, and User classes
    - Infinite loop handles menu and user actions
    """
    print("\n")
    print(logo)
    print("\n")

    color_print("\nWelcome to Rabit Hole Libary!\n", "green")

    if authenticated == False:
        authenticate()
    else:
        # Core objects
        book = classes.Book()
        staff = classes.Staff()
        user = classes.User()

        # Main loop
        while True:
            menu()
            choice = input(":>>>")
            match choice:
                case "1":
                    # View all books
                    book = classes.Book()
                    for book in book.all():
                        details = (
                            f"ID: {book['id']}, Title: {book['title']}, "
                            f"Author: {book['author_title']} {book['author_firstname']} {book['author_lastname']}, "
                            f"Publisher: {book['publisher_details']['name']}, "
                            f"Year Published: {book['year_published']}, "
                            f"Serial Number: {book['serial_num']}, Genre: {book['genre']}"
                        )
                        # color_print(details, "green")  # alternate color output
                        print(details)

                case "2":
                    # Add a new book (option to add new publisher as well)
                    color_print("ADD NEW BOOK", "green")
                    color_print("Please fill up the details bellow:", "green")
                    title = input("Book Title: ")
                    author_title = input("Author Title: ")
                    author_firstname = input("Author Firstname: ")
                    author_lastname = input("Author Lastname: ")

                    # Show existing publishers for selection
                    print("\nPlease Select Publisher. Enter ID")
                    for a in pub_details:
                        print(a)
                    print(
                        "\nIf you cannot find the publisher you are looking for, enter 'new'"
                    )

                    publisher_id_ = input("Publisher ID: ")
                    match publisher_id_:
                        case "new":
                            # Add a new publisher if not listed
                            publisher = classes.Publisher()
                            color_print("\nAdding New Publisher\n", "green")
                            publisher_name = input("New Publisher Name: ")
                            year_established = input("Year Established: ")
                            publisher_id_ = publisher.add(
                                publisher_name, year_established
                            )["id"]

                    serial_num = input("Book Serial Number: ")
                    genre = input("Book Genre: ")
                    year_published = input("Year of Publication: ")

                    # Create book record using staff object
                    staff.new_book(
                        title,
                        author_firstname,
                        author_title,
                        author_lastname,
                        publisher_id_,
                        serial_num,
                        genre,
                        year_published,
                    )

                case "3":
                    # Delete an existing book
                    color_print("DELETE BOOK", "red")
                    book_id = input("Enter Book ID: ")
                    staff.delete_book(auth_staff["id"], auth_staff["psw"], book_id)

                case "4":
                    # Add new library user
                    color_print("Add New Libary User", "green")
                    color_print("Please fill up the details bellow:", "green")
                    fullname = input("Enter Fullname: ")
                    email = input("Enter Email: ")
                    phone = input("Enter Phone: ")
                    staff.add_user(
                        auth_staff["id"], auth_staff["psw"], fullname, email, phone
                    )

                case "5":
                    # Book search functionality with multiple filters
                    color_print("Search Books", "green")
                    opt_text = (
                        "\nHow would you like to search?\n"
                        "1. By Title \n2. By Author Name \n3. By Publisher \n4. By Genre \n5. By Year"
                    )
                    color_print(opt_text, "green")
                    choice = input(":>>>")
                    match choice:
                        case "1":
                            color_print("Search By Title", "green")
                            search_text = input("Enter Search Term: ")
                            staff.search(
                                auth_staff["id"],
                                auth_staff["psw"],
                                "title",
                                search_text,
                            )
                        case "2":
                            color_print("Search By Author Name", "green")
                            search_text = input("Enter Search Term: ")
                            staff.search(
                                auth_staff["id"],
                                auth_staff["psw"],
                                "author_name",
                                search_text,
                            )
                        case "3":
                            color_print("Search By Publisher", "green")
                            search_text = input("Enter Search Term: ")
                            staff.search(
                                auth_staff["id"],
                                auth_staff["psw"],
                                "publisher",
                                search_text,
                            )
                        case "4":
                            color_print("Search By Genre", "green")
                            search_text = input("Enter Search Term: ")
                            staff.search(
                                auth_staff["id"],
                                auth_staff["psw"],
                                "genre",
                                search_text,
                            )
                        case "5":
                            color_print("Search By Year", "green")
                            search_text = input("Enter Search Term: ")
                            staff.search(
                                auth_staff["id"], auth_staff["psw"], "year", search_text
                            )

                case "6":
                    # Borrow a book for a user
                    color_print("Borrow Book For User", "green")
                    user_id = input("Enter User ID: ")
                    book_id = input("Enter Book ID: ")
                    due = input("Enter Due Date (m/d/y): ")
                    staff.borrow_book(
                        auth_staff["id"], auth_staff["psw"], user_id, book_id, due
                    )

                case "7":
                    # Return a borrowed book
                    color_print("Return Book For User", "green")
                    user_id = input("Enter User ID: ")
                    book_id = input("Enter Book ID: ")
                    staff.return_book(
                        auth_staff["id"], auth_staff["psw"], user_id, book_id
                    )

                case "8":
                    # View a user profile by ID
                    color_print("View User By ID\n", "green")
                    user_id = input("Enter User ID: ")
                    staff.view_user(auth_staff["id"], auth_staff["psw"], user_id)

                case "9":
                    # Exit system gracefully
                    color_print("Shutting Down", "red")
                    exit()

                case __:
                    # Invalid choice -> loop continues
                    continue


# Program entry point
start()
