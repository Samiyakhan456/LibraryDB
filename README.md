# LibraryDB — MySQL Library Management System

A **Library Management System** built with **MySQL** and **Python** to manage books, members, borrowing activity, and overdue fines. The project includes a relational database schema, sample data, analytical SQL queries, and a Python CLI application for interacting with the database.

## Project Highlights

* Designed a **4-table relational schema**: `Books`, `Members`, `Borrowings`, and `Fines`
* Implemented **primary keys** and **foreign key constraints**
* Inserted realistic sample data for books, members, and borrowing records
* Wrote SQL queries for common library operations such as:

  * currently borrowed books
  * overdue members
  * most borrowed book
  * member borrowing history
  * overdue fines at **₹10/day**
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

### `fines`

Stores overdue fine information for borrowed books.

* `fine_id` — unique fine record ID
* `borrow_id` — references `borrowings(borrow_id)`
* `fine_amount` — overdue fine amount
* `days_overdue` — number of days the book is overdue
* `paid` — whether the fine has been paid

## SQL Queries Implemented

1. **Books currently borrowed**
   Returns all books that have not yet been returned.

2. **Members with overdue books**
   Finds members whose borrowed books are overdue and still unreturned.

3. **Most borrowed book**
   Identifies the book borrowed the highest number of times.

4. **Member borrowing history**
   Shows all books borrowed by a specific member along with borrowing and return details.

5. **Overdue fines calculation**
   Calculates overdue fines for unreturned books using the rule:

```text id="kpnhf4"
Fine = Days Overdue × ₹10
```

## Python CLI Features

The project includes an `app.py` file that connects to the MySQL database and provides a terminal menu to:

1. View all books
2. View currently borrowed books
3. View overdue members
4. View borrowing history of a specific member
5. View overdue fines
6. Exit

## Sample Fine Query

```sql id="x3rx5v"
SELECT 
    b.borrow_id,
    m.name AS member_name,
    bk.title AS book_title,
    b.due_date,
    DATEDIFF(CURDATE(), b.due_date) AS days_overdue,
    DATEDIFF(CURDATE(), b.due_date) * 10 AS fine_amount
FROM borrowings b
JOIN members m ON b.member_id = m.member_id
JOIN books bk ON b.book_id = bk.book_id
WHERE b.returned_at IS NULL
  AND b.due_date < CURDATE();
```

## Tech Stack

* **MySQL**
* **MySQL Workbench**
* **Python**
* **mysql-connector-python**
* **python-dotenv**

## Project Structure

```text id="szj6t8"
LibraryDB/
├── schema_and_data.sql
├── app.py
├── README.md
├── .gitignore
└── .env   # local only, not pushed to GitHub
```

## How to Run the Project

### 1. Clone the repository

```bash id="3xymlm"
git clone https://github.com/Samiyakhan456/LibraryDB.git
cd LibraryDB
```

### 2. Set up the MySQL database

* Open `schema_and_data.sql` in MySQL Workbench
* Run the script to create the `LibraryDB` database, tables, and sample data
* If not already included in `schema_and_data.sql`, create the `fines` table manually

### 3. Install Python dependencies

```bash id="d4a1k4"
python -m pip install mysql-connector-python python-dotenv
```

### 4. Create a `.env` file

Create a `.env` file in the project root with:

```env id="uvfx1w"
MYSQL_PASSWORD=your_mysql_password
```

### 5. Run the Python app

```bash id="ltpfpv"
python app.py
```

## Learning Outcomes

Through this project, I practiced:

* relational database design
* writing SQL DDL and DML statements
* defining primary and foreign key relationships
* using joins, filtering, and aggregation queries
* calculating overdue fees using SQL date functions
* connecting Python to a MySQL database
* keeping credentials secure with `.env` and `.gitignore`

## Future Improvements

* Add functionality to **borrow and return books directly from the Python app**
* Automatically update book availability when books are borrowed or returned
* Add fine payment tracking and payment status updates
* Normalize the schema further with separate `Authors` and `Categories` tables
* Build a frontend interface connected to the database

## Author

**Samiya Khan**
