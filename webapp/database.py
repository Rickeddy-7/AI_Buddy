import sqlite3

class LiteracyLabDatabase:
    
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    
    def create_tables(self):
        students = """CREATE TABLE students(
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT(25),
            surname TEXT(25),
            id_number INTEGER,
            password INTEGER,
            grade TEXT(2),
            parent_id INTEGER,
            FOREIGN KEY(parent_id) REFERENCES parents
        );"""
        educators = """CREATE TABLE teachers(
            educator_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT(25),
            surname TEXT(25),
            id_number INTEGER,
            password INTEGER,
            discipline TEXT(30)
        );"""
        parents = """CREATE TABLE parents(
            parent_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT(25),
            surname TEXT(25),
            id_number INTEGER,
            phone_number TEXT(10),
            child_id INTEGER,
            FOREIGN KEY(child_id) REFERENCES students
        );"""
        
        self.cursor.execute(students)
        self.cursor.execute(educators)
        self.cursor.execute(parents)
        self.conn.commit()
    

    def add_student(self, values):
        insert = """INSERT INTO students (first_name, surname, id_number, password, grade, parent_id) VALUES (?, ?, ?, ?, ?, ?);"""
        self.cursor.execute(insert, values)
        self.conn.commit()


    def add_educator(self, values):
        insert = """INSERT INTO teachers (first_name, surname, id_number, password, discipline) VALUES (?, ?, ?, ?, ?);"""
        self.cursor.execute(insert, values)
        self.conn.commit()
    

    def add_parent(self, values):
        insert = """INSERT INTO parents (first_name, surname, id_number, phone_number, child_id) VALUES (?, ?, ?, ?, ?);"""
        self.cursor.execute(insert, values)
        self.conn.commit()
    

    def validate_student(self, values):
        select = """SELECT * FROM students WHERE id_number = ? AND first_name = ?"""
        return self.cursor.execute(select, values).fetchall()
    
   
    def close_connection(self):
        self.conn.close()
