import sqlite3

CREATE_TODO_TABLE = """CREATE TABLE IF NOT EXIST todo(
                        id          INTEGER PRIMARY KEY,
                        name        TEXT NOT NULL,
                        date        DATE NOT NULL,
                        priority    INTEGER
                        done        varchar(1) DEFAULT 'N')"""

ADD_JOB = """INSERT INTO todo(name, date, priority) VALUES (?,?,?);"""


def create_connection():
    return sqlite3.connect("data.db")

def create_table(connection):
    with connection:
        connection.execute(CREATE_TODO_TABLE)

def add_job(connection, name, date, priority):
    with connection:
        connection.execute(ADD_JOB, (name, date, priority))
    
