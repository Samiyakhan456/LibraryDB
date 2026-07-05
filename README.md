# LibraryDB — MySQL Library Management System

A **Library Management System** built with **MySQL** and **Python** to manage books, members, and borrowing activity. The project includes a relational database schema, sample data, analytical SQL queries, and a Python CLI application for interacting with the database.

## Project Highlights

* Designed a **3-table relational schema**: `Books`, `Members`, and `Borrowings`
* Implemented **primary keys** and **foreign key constraints**
* Inserted realistic sample data for books, members, and borrowing records
* Wrote SQL queries for common library operations such as:

  * currently borrowed books
  * overdue members
  * most borrowed book
  * member borrowing history
* Built a **Python CLI application (`app.py`)** to interact with the database directly from the terminal

## Database Schema

### `books`

Stores information about books in the library.

* `book_id` — unique book ID
* `title` — book title
* `author` — author name
* `published_year` — year of publication
* `available` — availability status

### `members`

Stores information about registered library members.

* `member_id` — unique member ID
* `name` — member name
* `email` — member email
* `joined_date` — date the member joined

### `borrowings`

Stores borrowing records linking members and books.

* `borrow_id` — unique borrowing ID
* `book_id` — references `books(book_id)`
* `member_id` — references `members(member_id)`
* `borrowed_at` — borrowing timestamp
* `returned_at` — return timestamp
* `due_date` — due date for return

## SQL Queries Implemented

1. **Books currently borrowed**
   Returns all books that have not yet been returned.

2. **Members with overdue books**
   Finds members whose borrowed books are overdue and still unreturned.

3. **Most borrowed book**
   Identifies the book borrowed the highest number of times.

4. **Member borrowing history**
   Shows all books borrowed by a specific member along with borrowing and return details.

## Python CLI Features

The project includes an `app.py` file that connects to the MySQL database and provides a simple terminal menu to:

1. View all books
2. View currently borrowed books
3. View overdue members
4. View borrowing history of a specific member

## Sample Query

```sql
SELECT books.title,
       members.name,
       borrowings.borrowed_at,
       borrowings.due_date
FROM borrowings
JOIN books ON borrowings.book_id = books.book_id
JOIN members ON borrowings.member_id = members.member_id
WHERE borrowings.returned_at IS NULL;
```

## Tech Stack

* **MySQL**
* **MySQL Workbench**
* **Python**
* **mysql-connector-python**
* **python-dotenv**

## Project Structure

```text
LibraryDB/
├── schema_and_data.sql
├── app.py
├── README.md
├── .gitignore
└── .env   # local only, not pushed to GitHub
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Samiyakhan456/LibraryDB.git
cd LibraryDB
```

### 2. Set up the MySQL database

* Open `schema_and_data.sql` in MySQL Workbench
* Run the script to create the `LibraryDB` database, tables, and sample data

### 3. Install Python dependencies

```bash
python -m pip install mysql-connector-python python-dotenv
```

### 4. Create a `.env` file

Create a `.env` file in the project root with:

```env
MYSQL_PASSWORD=your_mysql_password
```

### 5. Run the Python app

```bash
python app.py
```

## Learning Outcomes

Through this project, I practiced:

* relational database design
* writing SQL DDL and DML statements
* defining primary and foreign key relationships
* using joins, filtering, and aggregation queries
* connecting Python to a MySQL database
* keeping credentials secure with `.env` and `.gitignore`

## Future Improvements

* Add separate `Authors` and `Categories` tables for better normalization
* Add a `Fines` table for overdue returns
* Add functionality to borrow/return books directly from the Python app
* Build a frontend interface connected to the database

## Author

**Samiya Khan**
