-- Q1: readers with at least two loans.
SELECT r.reader_id, r.name, COUNT(l.loan_id) AS total
FROM readers r JOIN loans l ON l.reader_id = r.reader_id
GROUP BY r.reader_id, r.name HAVING COUNT(l.loan_id) >= 2
ORDER BY r.reader_id;

-- Q2: include readers with zero loans.
SELECT r.reader_id, r.name, COUNT(l.loan_id) AS total
FROM readers r LEFT JOIN loans l ON l.reader_id = r.reader_id
GROUP BY r.reader_id, r.name ORDER BY r.reader_id;

-- Q3: books never borrowed.
SELECT b.book_id, b.title FROM books b
WHERE NOT EXISTS (SELECT 1 FROM loans l WHERE l.book_id = b.book_id)
ORDER BY b.book_id;

-- Q4: active loans.
SELECT loan_id, name, title FROM open_loans ORDER BY loan_id;
