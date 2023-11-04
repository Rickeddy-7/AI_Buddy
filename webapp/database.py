
import sqlite3



def connect_to_database():
    '''established a connection to the literacy lab database'''

    return sqlite3.connect("literacy_lab.db")


def create_tables(cursor: sqlite3.Cursor):
    '''creates the schema(s) of the database'''

    students = """CREATE TABLE students(
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT(25),
            surname TEXT(25),
            id_number INTEGER,
            password INTEGER,
            grade TEXT(2),
            parent_id INTEGER,
            FOREIGN KEY(parent_id) REFERENCES parents
        );
    """
    educators = """CREATE TABLE educators(
            educator_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT(25),
            surname TEXT(25),
            id_number INTEGER,
            password INTEGER,
            dicsipline TEXT(30)
        );
    """
    parents = """CREATE TABLE parents(
            parent_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT(25),
            surname TEXT(25),
            id_number INTEGER,
            phone_number TEXT(10),
            child_id INTEGER,
            FOREIGN KEY(child_id) REFERENCES students
        );
    """
    
    cursor.execute(students)
    cursor.commit()
    cursor.execute(educators)
    cursor.commit()
    cursor.execute(parents)
    cursor.commit()


def add_student(cursor: sqlite3.Cursor, values: list):
    '''adds a students' credentials to the database'''

    insert = """INSERT INTO students (first_name, surname, id_number, password, grade, parent_id) VALUES (?, ?, ?, ?, ?, ?);"""
    
    cursor.execute(insert, values).commit()


def add_educator(cursor: sqlite3.Cursor, values: list):
    '''adds a students' credentials to the database'''

    insert = """INSERT INTO educators (first_name, surname, id_number, password, dicsipline) VALUES (?, ?, ?, ?, ?);"""
    
    cursor.execute(insert, values).commit()


def add_parent(cursor: sqlite3.Cursor, values: list):
    '''adds a students' credentials to the database'''

    insert = """INSERT INTO parents (first_name, surname, id_number, phone_number, child_id) VALUES (?, ?, ?, ?, ?);"""
    
    cursor.execute(insert, values).commit()
