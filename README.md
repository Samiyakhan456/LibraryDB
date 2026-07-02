# LibraryDB — MySQL Library Management System

A relational database project built in **MySQL** to manage books, members, and borrowing activity in a library system. The project focuses on database design, foreign key relationships, sample data generation, and analytical SQL queries for common library operations.

## Project Highlights

* Designed a **3-table relational schema**: `Books`, `Members`, and `Borrowings`
* Implemented **primary keys** and **foreign key constraints**
* Inserted realistic sample data for books, members, and borrowing records
* Wrote SQL queries to answer practical library-management questions such as:

  * currently borrowed books
  * overdue books
  * most borrowed book
  * member borrowing history

## Database Schema

### `books`

Stores information about books available in the library.

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

Stores records of books borrowed by members.

* `borrow_id` — unique borrowing ID
* `book_id` — references `books(book_id)`
* `member_id` — references `members(member_id)`
* `borrowed_at` — borrowing timestamp
* `returned_at` — return timestamp
* `due_date` — due date for return

## Example Queries Implemented

### 1. Books currently borrowed

Returns all books that have not yet been returned.

### 2. Members with overdue books

Finds members whose books are overdue and still unreturned.

### 3. Most borrowed book

Identifies the book borrowed the highest number of times.

### 4. Member borrowing history

Shows all books borrowed by a specific member along with borrow/return details.

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
* **SQL**

## Files

* `schema_and_data.sql` — database creation, table creation, sample inserts, and queries
* `README.md` — project documentation

## Learning Outcomes

Through this project, I practiced:

* relational database design
* writing SQL DDL and DML statements
* defining primary and foreign key relationships
* using joins to combine data across tables
* writing filtering and aggregation queries for real-world use cases

## Future Improvements

* Add separate `Authors` and `Categories` tables for normalization
* Add a `Fines` table for overdue returns
* Create views or stored procedures for common operations
* Build a frontend interface connected to the database

## Author

**Samiya Khan**
