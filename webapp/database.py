
import os
import socketserver
import openai
import sqlite3

openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_key = "37635d8c1d7349fe8698c3d77f855d2e"
openai.api_base = "https://literacylab.openai.azure.com/"


response = openai.ChatCompletion.create(
    engine="literacylab",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who were the founders of Microsoft?"}
    ]
)

# print(response)
print(f"Clean:\n{response['choices'][0]['message']['content']}")


class Handler():
    def connect_to_database():
        '''established a connection to the azure database'''

        connection = sqlite3.connect("ai_buddy.db")
        return connection.cursor()


    def create_tables(cursor):
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
        
        cursor.execute(students).commit()
        cursor.execute(educators).commit()
        cursor.execute(parents).commit()


    def add_student(cursor, values: list):
        '''adds a students' credentials to the database'''

        insert = """INSERT INTO students (first_name, surname, id_number, password, grade, parent_id) VALUES (?, ?, ?, ?, ?, ?);"""
        
        cursor.execute(insert, values).commit()


    def add_educator(cursor, values: list):
        '''adds a students' credentials to the database'''

        insert = """INSERT INTO educators (first_name, surname, id_number, password, dicsipline) VALUES (?, ?, ?, ?, ?);"""
        
        cursor.execute(insert, values).commit()


    def add_parent(cursor, values: list):
        '''adds a students' credentials to the database'''

        insert = """INSERT INTO parents (first_name, surname, id_number, phone_number, child_id) VALUES (?, ?, ?, ?, ?);"""
        
        cursor.execute(insert, values).commit()


def start_server():
    '''start the server and accept requests from the form'''

    PORT = 8000
    with socketserver.TCPServer(('127.0.0.1', PORT), Handler) as s:
        print(f'Server running and listening on port {PORT}...\n')
        s.serve_forever() # this method will call do_POST upon invocation



if __name__ == "__main__":
    start_server()