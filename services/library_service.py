from database.db import get_connection


class LibraryService:

    def add_book(self, book):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO books VALUES (?, ?, ?, ?)",
            (book.id, book.title, book.author, 1)
        )

        conn.commit()
        conn.close()

    def get_books(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "id": r[0],
                "title": r[1],
                "author": r[2],
                "available": bool(r[3])
            } for r in rows
        ]

    def issue_book(self, book_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE books SET available = 0 WHERE id = ? AND available = 1",
            (book_id,)
        )

        conn.commit()
        updated = cursor.rowcount
        conn.close()

        return updated > 0

    def return_book(self, book_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE books SET available = 1 WHERE id = ?",
            (book_id,)
        )

        conn.commit()
        updated = cursor.rowcount
        conn.close()

        return updated > 0
