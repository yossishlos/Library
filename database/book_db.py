from database.db_connection import DB

class BookDB:
    def __init__(self, db: DB):
        self.db = db
        self.db.get_connection()


    def create_book(self, data: dict):
        try:
            self.db.cursor.execute("""
    INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)
    """, (data["title"], data["author"], data["genre"]))
            self.db.connection.commit()
            return {"message" : "good"}
        except Exception as e:
            print(e)


    def get_all_books(self):
        try:
            self.db.cursor.execute("""
    select * from books
    """)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def get_book_by_id(self, id: int):
        try:
            self.db.cursor.execute("""
    select * from books where id = %s
    """, (id,))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def update_book(self, id: int, data: dict):
        try:
            self.db.cursor.execute("""
    update books set title = %s, author = %s, genre = %s where id = %s
    """, (data["title"], data["author"], data["genre"], id))
            self.db.connection.commit()
            return {"message" : "good"}
        except Exception as e:
            print(e)


    def set_available(self, id: int, val: bool, member_id: int):
        try:
            self.db.cursor.execute("""
    UPDATE books SET is_available = %s, borrowed_by_member_id = %s where id = %s
    """, (val, member_id, id))
            self.db.connection.commit()
            return {"message" : "good"}
        except Exception as e:
            print(e)


    def count_total_books(self):
        try:
            self.db.cursor.execute("""
    select count(*) from books
    """)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def count_available_books(self):
        try:
            self.db.cursor.execute("""
    select count(is_available) from books where is_available = true
    """)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def count_borrowed_books(self):
        try:
            self.db.cursor.execute("""
    select count(is_available) from books where is_available = false
    """)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def count_by_genre(self, genre):
        try:
            self.db.cursor.execute("""
    SELECT genre, COUNT(*) FROM books GROUP BY genre
    """)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    
    def count_active_borrows_by_member(self, member_id):
        try:
            self.db.cursor.execute("""
    
    """)
        except Exception as e:
            print(e)