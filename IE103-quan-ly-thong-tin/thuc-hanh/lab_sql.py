"""Self-contained SQLite/XML teaching lab. No disk database is written."""
from pathlib import Path
import sqlite3
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
EXPECTED = [
    [(1, "An", 2), (2, "Binh", 2)],
    [(1, "An", 2), (2, "Binh", 2), (3, "Chi", 1), (4, "Dung", 0)],
    [("B04", "Mang may tinh")],
    [(2, "An", "Co so du lieu"), (3, "Binh", "He dieu hanh"),
     (5, "Chi", "Dai so tuyen tinh")],
]


def build_database():
    connection = sqlite3.connect(":memory:")
    connection.executescript((HERE / "schema.sql").read_text(encoding="utf-8"))
    return connection


def run_lab():
    connection = build_database()
    try:
        statements = (HERE / "queries.sql").read_text(encoding="utf-8").split(";")
        results = [connection.execute(sql).fetchall() for sql in statements if sql.strip()]
        assert results == EXPECTED, (results, EXPECTED)
        for index, rows in enumerate(results, 1):
            print("Q{}: {}".format(index, rows))

        # Trigger must reject a second concurrent open loan for B01.
        try:
            connection.execute(
                "INSERT INTO loans VALUES (?, ?, ?, ?, ?)",
                (6, 4, "B01", "2025-10-07", None),
            )
        except sqlite3.IntegrityError:
            connection.rollback()
        else:
            raise AssertionError("Duplicate open loan was accepted")

        # Show transaction rollback without changing the baseline.
        connection.execute("BEGIN")
        connection.execute("UPDATE readers SET name = ? WHERE reader_id = ?", ("Changed", 1))
        connection.rollback()
        assert connection.execute("SELECT name FROM readers WHERE reader_id = 1").fetchone() == ("An",)

        # Parameter binding treats the input as a value, not SQL syntax.
        payload = "' OR 1=1 --"
        assert connection.execute("SELECT * FROM readers WHERE name = ?", (payload,)).fetchall() == []

        tree = ET.parse(HERE / "library.xml")
        title = tree.getroot().find("./book[@id='B01']/title").text
        assert title == "He dieu hanh"
        print("XML title:", title)
        print("PASS: queries, trigger, rollback, parameter binding, XML")
    finally:
        connection.close()


if __name__ == "__main__":
    run_lab()
