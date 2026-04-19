<!-- ══════════════════════════════════════════════════════════════ -->
<!--               Rabbit Hole Library System · README              -->
<!-- ══════════════════════════════════════════════════════════════ -->

<div align="center">

# Smart Library System

**A Python-based Library Management System** built as a final project
for the Python Session in a Cyber Security Course at **HiiT**.

Lightweight but feature-rich — designed to manage a library efficiently
with both **staff** and **user** functionalities.

</div>

---

## 📖 Features

### ✅ Book Management

Manage books in the library with full detail tracking.

Each book entry contains:

| Field | Description |
|-------|-------------|
| Title | Book title |
| Author | Title, first name, last name |
| Publisher | Name & year established |
| Publishing Year | Year of release |
| Serial Number | Unique identifier |
| Genre / Category | Classification tag |

---

### 🔍 Book Search & Filter

Find books by any of the following:

- 📌 Title
- 👤 Author name
- 🏢 Publisher
- 🏷️ Genre / Category
- 📅 Year of publication

---

### 👩‍💼 Staff Features

- Register library users
- Delete books from the system
- Track borrowed and returned books

---

### 👤 User Features

- Borrow and return books
- View personal borrowing history

---

## 🗄️ Database Structure

The system uses a **Python dictionary-based** database structure to store:

```
📦 Database
 ├── 📚 Books
 ├── 🧑‍💼 Staff Members
 ├── 👤 Library Users
 ├── 🏢 Publishers
 └── 📋 Borrowing Records
```

This allows flexibility in managing and expanding the system.

---

## 🛠️ Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt
```

`requirements.txt` includes:

```
colorama==0.4.6
pyfiglet==1.0.3
termcolor==3.1.0
```

---

## 🚀 Getting Started

**1.** Clone or download the project

**2.** Install dependencies:

```bash
pip install -r requirements.txt
```

**3.** Run the script:

```bash
python main.py
```

---

## 🎯 Special Notes

> This project was completed as the **final project** for the Python Session in my Cyber Security Course at **HiiT**.

- Special credit goes to **Mr. Godwin**, our passionate teacher, who takes the time to ensure we fully understand the concepts.
- This course has significantly improved my programming skills, allowing me to solve problems more easily and approach projects with an **OOP mindset** — without breaking my head! 😄

---

## 📌 To-Do / Future Enhancements

- [ ] Add support for exporting database to external files (JSON/CSV)
- [ ] Implement a simple authentication layer for staff and users
- [ ] Add due date reminders for borrowed books
- [ ] Enhance search with partial matching (e.g., fuzzy search)
- [ ] Create a basic GUI version for better interaction

---

## 🏷️ Keywords

`Python Library System` · `Library Management Python` · `Book Borrowing Script` · `Python Final Project` · `Cyber Security Course Projects` · `Rabbit Hole Library` · `Python OOP Projects` · `Library Staff User System` · `Python Database Project` · `Educational Library Script`

---

## 📚 License

This project is open-source and free to use for **learning and educational purposes**.
