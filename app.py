import os
from dotenv import load_dotenv
import mysql.connector

# Load variables from .env
load_dotenv()


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="LibraryDB"
    )


def view_all_books(cursor):
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


def main():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        while True:
            print("\n====== LibraryDB Menu ======")
            print("1. View all books")
            print("2. View currently borrowed books")
            print("3. View overdue members")
            print("4. View member borrowing history")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                view_all_books(cursor)
            elif choice == "2":
                view_borrowed_books(cursor)
            elif choice == "3":
                view_overdue_members(cursor)
            elif choice == "4":
                view_member_history(cursor)
            elif choice == "5":
                print("Exiting LibraryDB. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print("Database Error:", err)


if __name__ == "__main__":
    main()
