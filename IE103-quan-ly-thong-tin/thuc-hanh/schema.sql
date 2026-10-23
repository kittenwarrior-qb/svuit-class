PRAGMA foreign_keys = ON;

CREATE TABLE readers (
    reader_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE books (
    book_id TEXT PRIMARY KEY NOT NULL,
    title TEXT NOT NULL,
    published_year INTEGER NOT NULL CHECK (published_year BETWEEN 1000 AND 9999)
);
CREATE TABLE loans (
    loan_id INTEGER PRIMARY KEY,
    reader_id INTEGER NOT NULL REFERENCES readers(reader_id),
    book_id TEXT NOT NULL REFERENCES books(book_id),
    borrowed_on TEXT NOT NULL,
    returned_on TEXT,
    CHECK (returned_on IS NULL OR returned_on >= borrowed_on)
);
CREATE INDEX ix_loans_reader ON loans(reader_id);

-- Teaching trigger: one physical book cannot have two open loans.
-- UPDATE is covered too, so changing a closed loan back to open is checked.
CREATE TRIGGER prevent_duplicate_open_insert
BEFORE INSERT ON loans
WHEN NEW.returned_on IS NULL
AND EXISTS (SELECT 1 FROM loans WHERE book_id = NEW.book_id AND returned_on IS NULL)
BEGIN
    SELECT RAISE(ABORT, 'book already borrowed');
END;
CREATE TRIGGER prevent_duplicate_open_update
BEFORE UPDATE ON loans
WHEN NEW.returned_on IS NULL
AND EXISTS (
    SELECT 1 FROM loans
    WHERE book_id = NEW.book_id AND returned_on IS NULL AND loan_id <> OLD.loan_id
)
BEGIN
    SELECT RAISE(ABORT, 'book already borrowed');
END;

INSERT INTO readers VALUES (1, 'An'), (2, 'Binh'), (3, 'Chi'), (4, 'Dung');
INSERT INTO books VALUES
    ('B01', 'He dieu hanh', 2022),
    ('B02', 'Co so du lieu', 2020),
    ('B03', 'Dai so tuyen tinh', 2023),
    ('B04', 'Mang may tinh', 2021);
INSERT INTO loans VALUES
    (1, 1, 'B01', '2025-10-01', '2025-10-05'),
    (2, 1, 'B02', '2025-10-02', NULL),
    (3, 2, 'B01', '2025-10-06', NULL),
    (4, 2, 'B03', '2025-10-03', '2025-10-04'),
    (5, 3, 'B03', '2025-10-05', NULL);

CREATE VIEW open_loans AS
SELECT l.loan_id, r.name, b.title
FROM loans AS l JOIN readers AS r ON l.reader_id = r.reader_id
JOIN books AS b ON l.book_id = b.book_id
WHERE l.returned_on IS NULL;
