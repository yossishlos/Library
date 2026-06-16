import mysql.connector

class DB:
    def __init__(self, config: dict={
        "host" : "localhost",
        "user" : "root",
        "password" : "secret",
        "database" : "library_db"
    }):
        self.config = config
        self.connection = None
        self.cursor = None

    def get_connection(self):
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor(dictionary=True)
        # self.cursor.execute("create database if not exists library_db")
        # self.cursor.execute("use library_db")

    def create_table(self):
        self.cursor.execute("""CREATE TABLE if not exists books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    genre ENUM ("Fiction", "Non-Fiction", "Science", "History", "Other") NOT NULL,
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    borrowed_by_member_id INT DEFAULT NULL 
    ); """)
        
        self.cursor.execute("""CREATE TABLE if not exists members(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    total_borrows INT NOT NULL DEFAULT 0
    ); """)

    def disconnect(self):

        self.connection.close()
        self.cursor.close()