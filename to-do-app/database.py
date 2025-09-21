import sqlite3

CREATE_TODO_TABLE = """CREATE TABLE IF NOT EXISTS todo(
                        id          INTEGER PRIMARY KEY,
                        name        TEXT NOT NULL,
                        date        DATE NOT NULL,
                        priority    INTEGER,
                        done        varchar(1) DEFAULT 'N')"""

ADD_JOB = """INSERT INTO todo(name, date, priority) VALUES (?,?,?);"""

UPDATE_JOB = """UPDATE todo SET done = 'S' WHERE name = ? AND date = ?;"""

SEE_JOB_SPECIFIC_DAY = """SELECT * FROM todo WHERE date = ? ORDER BY priority ASC"""

def create_connection():
    return sqlite3.connect("data.db")

def create_table(connection):
    with connection:
        connection.execute(CREATE_TODO_TABLE)

def add_job(connection, name, date, priority):
    with connection:
        connection.execute(ADD_JOB, (name, date, priority))

def check_done(connection,name,date):
    with connection:
        connection.execute(UPDATE_JOB, (name, date))

def see_job_specific_day(connection,date):
    with connection:
        return connection.execute(SEE_JOB_SPECIFIC_DAY, (date,)).fetchall()
    
def close_connection(connection):
    connection.close() #create a database, if the file doesn't exist it creates the file