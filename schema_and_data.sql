USE LibraryDB;
DROP TABLE IF EXISTS Borrowings;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Books;
CREATE TABLE books (
	book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    published_year INTEGER,
    available BOOLEAN DEFAULT TRUE
    );
CREATE TABLE members (
     member_id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(100) NOT NULL,
     email VARCHAR(255) UNIQUE,
     joined_date DATE DEFAULT (CURRENT_DATE)
     );
CREATE TABLE borrowings (
	 borrow_id INT AUTO_INCREMENT PRIMARY KEY,
     book_id INT NOT NULL,
     member_id INT NOT NULL,
     borrowed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     returned_at TIMESTAMP NULL,
     due_date DATE,
     FOREIGN KEY (book_id) REFERENCES books(book_id),
     FOREIGN KEY (member_id) REFERENCES members(member_id)
     );

INSERT INTO Books (title, author, published_year, available)
VALUES
('The Alchemist', 'Paulo Coelho', 1988, TRUE),
('Atomic Habits', 'James Clear', 2018, TRUE),
('Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 1997, TRUE),
('The Hobbit', 'J.R.R. Tolkien', 1937, FALSE),
('To Kill a Mockingbird', 'Harper Lee', 1960, TRUE),
('1984', 'George Orwell', 1949, TRUE),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, FALSE),
('The Catcher in the Rye', 'J.D. Salinger', 1951, TRUE),
('Rich Dad Poor Dad', 'Robert Kiyosaki', 1997, TRUE),
('The Psychology of Money', 'Morgan Housel', 2020, TRUE);

INSERT INTO Members (name, email, joined_date)
VALUES
('Aarav Sharma', 'aarav.sharma@email.com', '2025-01-10'),
('Priya Patel', 'priya.patel@email.com', '2025-01-15'),
('Rahul Verma', 'rahul.verma@email.com', '2025-02-01'),
('Ananya Singh', 'ananya.singh@email.com', '2025-02-08'),
('Rohan Mehta', 'rohan.mehta@email.com', '2025-03-02'),
('Sneha Kapoor', 'sneha.kapoor@email.com', '2025-03-15'),
('Arjun Nair', 'arjun.nair@email.com', '2025-04-01'),
('Neha Gupta', 'neha.gupta@email.com', '2025-04-20'),
('Karan Malhotra', 'karan.malhotra@email.com', '2025-05-10'),
('Samiya Khan', 'samiya.khan@email.com', '2025-06-01');

INSERT INTO Borrowings
(book_id, member_id, borrowed_at, returned_at, due_date)
VALUES
(1, 2, '2025-06-01 10:00:00', '2025-06-10 16:00:00', '2025-06-15'),
(2, 5, '2025-06-05 09:30:00', NULL, '2025-06-20'),
(3, 1, '2025-06-07 14:00:00', '2025-06-18 11:00:00', '2025-06-21'),
(4, 8, '2025-06-10 13:20:00', NULL, '2025-06-24'),
(5, 3, '2025-06-12 15:00:00', '2025-06-19 10:30:00', '2025-06-26'),
(6, 6, '2025-06-15 11:00:00', NULL, '2025-06-29'),
(7, 10, '2025-06-18 09:15:00', NULL, '2025-07-02'),
(8, 4, '2025-06-20 16:45:00', '2025-06-27 12:00:00', '2025-07-04'),
(9, 7, '2025-06-22 10:10:00', NULL, '2025-07-06'),
(10, 9, '2025-06-25 17:30:00', NULL, '2025-07-09');
    
SELECT * FROM books;
SELECT * FROM Members;
SELECT * FROM borrowings;

SELECT books.title,
borrowings.borrowed_at 
FROM borrowings
JOIN books ON borrowings.book_id = books.book_id 
WHERE borrowings.returned_at IS NULL;

SELECT members.name,
       books.title,
       borrowings.due_date
FROM borrowings
JOIN members ON borrowings.member_id = members.member_id
JOIN books ON borrowings.book_id = books.book_id
WHERE borrowings.returned_at IS NULL
  AND borrowings.due_date < CURDATE();
  
SELECT books.title,
       COUNT(*) AS times_borrowed
FROM borrowings
JOIN books ON borrowings.book_id = books.book_id
GROUP BY books.book_id, books.title
ORDER BY times_borrowed DESC
LIMIT 1;

SELECT members.name,
       books.title,
       borrowings.borrowed_at,
       borrowings.returned_at,
       borrowings.due_date
FROM borrowings
JOIN members ON borrowings.member_id = members.member_id
JOIN books ON borrowings.book_id = books.book_id
WHERE members.name = 'Samiya Khan'
ORDER BY borrowings.borrowed_at DESC;