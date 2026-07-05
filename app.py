import os  # lets Python access environment variables like MYSQL_PASSWORD
from dotenv import load_dotenv  # loads variables from the .env file
import mysql.connector  # lets Python connect to and talk to a MySQL database

# Load variables from .env into Python's environment
load_dotenv()


# Creates and returns a connection to the MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",  # database is running on this computer
        user="root",  # MySQL username used to log in
        password=os.getenv("MYSQL_PASSWORD"),  # gets password from .env
        database="LibraryDB"  # database to use after connecting
    )


# Shows all books stored in the books table
def view_all_books(cursor):  # cursor runs SQL queries and fetches results from MySQL
    query = """
    SELECT book_id, title, author, published_year, available
    FROM books;
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\n--- All Books ---")
    if not rows:
        print("No books found.")
        return

    for row in rows:
        book_id, title, author, year, available = row
        status = "Available" if available else "Not Available"
        print(f"{book_id}. {title} | {author} | {year} | {status}")


# Shows books that are currently borrowed and not yet returned
def view_borrowed_books(cursor):
    query = """
    SELECT books.title,
           members.name,
           borrowings.borrowed_at,
           borrowings.due_date
    FROM borrowings
    JOIN books ON borrowings.book_id = books.book_id
    JOIN members ON borrowings.member_id = members.member_id
    WHERE borrowings.returned_at IS NULL;
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\n--- Currently Borrowed Books ---")
    if not rows:
        print("No borrowed books found.")
        return

    for row in rows:
        title, member_name, borrowed_at, due_date = row
        print(f"Book: {title} | Borrowed by: {member_name} | Borrowed at: {borrowed_at} | Due: {due_date}")


# Shows members whose borrowed books are overdue and still not returned
def view_overdue_members(cursor):
    query = """
    SELECT members.name,
           books.title,
           borrowings.due_date
    FROM borrowings
    JOIN members ON borrowings.member_id = members.member_id
    JOIN books ON borrowings.book_id = books.book_id
    WHERE borrowings.returned_at IS NULL
      AND borrowings.due_date < CURDATE();
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\n--- Overdue Members ---")
    if not rows:
        print("No overdue books found.")
        return

    for row in rows:
        member_name, title, due_date = row
        print(f"Member: {member_name} | Book: {title} | Due Date: {due_date}")


# Shows all borrowing records for a specific member
def view_member_history(cursor):
    member_name = input("Enter member name: ")

    query = """
    SELECT members.name,
           books.title,
           borrowings.borrowed_at,
           borrowings.returned_at,
           borrowings.due_date
    FROM borrowings
    JOIN members ON borrowings.member_id = members.member_id
    JOIN books ON borrowings.book_id = books.book_id
    WHERE members.name = %s
    ORDER BY borrowings.borrowed_at DESC;
    """
    cursor.execute(query, (member_name,))
    rows = cursor.fetchall()

    print(f"\n--- Borrowing History for {member_name} ---")
    if not rows:
        print("No borrowing history found for this member.")
        return

    for row in rows:
        name, title, borrowed_at, returned_at, due_date = row
        returned_text = returned_at if returned_at else "Not Returned"
        print(f"Book: {title} | Borrowed: {borrowed_at} | Returned: {returned_text} | Due: {due_date}")


# Shows overdue fines calculated at ₹10 per day for currently overdue books
def view_overdue_fines(cursor):
    query = """
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
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\n--- Overdue Fines (₹10/day) ---")
    if not rows:
        print("No overdue fines found.")
        return

    for row in rows:
        borrow_id, member_name, book_title, due_date, days_overdue, fine_amount = row
        print(
            f"Borrow ID: {borrow_id} | Member: {member_name} | "
            f"Book: {book_title} | Due: {due_date} | "
            f"Days Overdue: {days_overdue} | Fine: ₹{fine_amount}"
        )


# Main program menu
def main():
    try:
        conn = connect_db()  # open connection to MySQL
        cursor = conn.cursor()  # create cursor to run SQL queries

        while True:
            print("\n====== LibraryDB Menu ======")
            print("1. View all books")
            print("2. View currently borrowed books")
            print("3. View overdue members")
            print("4. View member borrowing history")
            print("5. View overdue fines")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                view_all_books(cursor)
            elif choice == "2":
                view_borrowed_books(cursor)
            elif choice == "3":
                view_overdue_members(cursor)
            elif choice == "4":
                view_member_history(cursor)
            elif choice == "5":
                view_overdue_fines(cursor)
            elif choice == "6":
                print("Exiting LibraryDB. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

        cursor.close()  # stop using the cursor
        conn.close()  # close the database connection

    except mysql.connector.Error as err:
        print("Database Error:", err)


# Runs the program when app.py is executed directly
if __name__ == "__main__":
    main()
