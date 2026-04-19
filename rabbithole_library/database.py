# Database for Rabbit Hole Library

database = [
    {
        "master_id": "123450",  # System-wide master account
        "master_password": "yoyoyo",

        "data": {
            "books": [
                {
                    "id": "B001",
                    "data_added": "20240910",
                    "title": "Drama of the Gifted Child",
                    "author_firstname": "Alice",
                    "author_title": "Dr.",
                    "author_lastname": "Miller",
                    "publisher_id": "P001",
                    "year_published": "1967",
                    "serial_num": "SN-0001",
                    "genre": "Psychology",
                    "publisher_details": {"id": "P001", "name": "Insight Press", "year_established": "1950"},
                },
                {
                    "id": "B002",
                    "data_added": "20240912",
                    "title": "The Rabbit Hole: A Journey into Knowledge",
                    "author_firstname": "John",
                    "author_title": "Prof.",
                    "author_lastname": "Doe",
                    "publisher_id": "P002",
                    "year_published": "2020",
                    "serial_num": "SN-0002",
                    "genre": "Non-Fiction",
                    "publisher_details": {"id": "P002", "name": "Knowledge House", "year_established": "2005"},
                },
                {
                    "id": "B003",
                    "data_added": "20240914",
                    "title": "The Great Gatsby",
                    "author_firstname": "F. Scott",
                    "author_title": "",
                    "author_lastname": "Fitzgerald",
                    "publisher_id": "P003",
                    "year_published": "1925",
                    "serial_num": "SN-0003",
                    "genre": "Classic Literature",
                    "publisher_details": {"id": "P003", "name": "Scribner", "year_established": "1846"},
                },
                {
                    "id": "B004",
                    "data_added": "20240915",
                    "title": "Python for Ethical Hackers",
                    "author_firstname": "Jane",
                    "author_title": "Ms.",
                    "author_lastname": "Smith",
                    "publisher_id": "P002",
                    "year_published": "2023",
                    "serial_num": "SN-0004",
                    "genre": "Technology",
                    "publisher_details": {"id": "P002", "name": "Knowledge House", "year_established": "2005"},
                },
                {
                    "id": "B005",
                    "data_added": "20240916",
                    "title": "1984",
                    "author_firstname": "George",
                    "author_title": "",
                    "author_lastname": "Orwell",
                    "publisher_id": "P004",
                    "year_published": "1949",
                    "serial_num": "SN-0005",
                    "genre": "Dystopian",
                    "publisher_details": {"id": "P004", "name": "Secker & Warburg", "year_established": "1935"},
                },
            ],

            "staffs": [
                {"fullname": "Alice Johnson", "email": "alice@library.com", "id": "S001", "psw": "alice123"},
                {"fullname": "Bob Williams", "email": "bob@library.com", "id": "S002", "psw": "bob456"},
                {"fullname": "Cynthia Lee", "email": "cynthia@library.com", "id": "S003", "psw": "cynthia789"},
            ],

            "users": [
                {
                    "lib_id": "U001",
                    "fullname": "Michael Brown",
                    "email": "michael.brown@gmail.com",
                    "phone": "+234-111-222-333",
                    "books_borrowed_ids": ["B001", "B003"],
                    "books_borrowed": [],
                    "date_added": "20240917",
                },
                {
                    "lib_id": "U002",
                    "fullname": "Sophia Turner",
                    "email": "sophia.turner@yahoo.com",
                    "phone": "+234-444-555-666",
                    "books_borrowed_ids": ["B004"],
                    "books_borrowed": [],
                    "date_added": "20240918",
                },
                {
                    "lib_id": "U003",
                    "fullname": "David Green",
                    "email": "david.green@hotmail.com",
                    "phone": "+234-777-888-999",
                    "books_borrowed_ids": [],
                    "books_borrowed": [],
                    "date_added": "20240919",
                },
            ],

            "publishers": [
                {"id": "P001", "name": "Insight Press", "year_established": "1950"},
                {"id": "P002", "name": "Knowledge House", "year_established": "2005"},
                {"id": "P003", "name": "Scribner", "year_established": "1846"},
                {"id": "P004", "name": "Secker & Warburg", "year_established": "1935"},
            ],

            "books_borrowed": [
                {
                    "lib_id": "U001",
                    "book_id": "B001",
                    "date_borrowed": "20240917",
                    "due_date": "20241001",
                },
                {
                    "lib_id": "U001",
                    "book_id": "B003",
                    "date_borrowed": "20240917",
                    "due_date": "20241001",
                },
                {
                    "lib_id": "U002",
                    "book_id": "B004",
                    "date_borrowed": "20240918",
                    "due_date": "20241002",
                },
            ],
        },
    }
]
