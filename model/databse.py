import sqlite3

#  this command creates a connection
conn = sqlite3.connect('students.db')

c = conn.cursor()  # my cursor

# creates a table
c.execute("""CREATE TABLE students (
            Name TEXT,
            Age INTEGER,
            GPA REAL,
            Siblings BOOLEAN
    )""")

c.execute("INSERT INTO students VALUES ('Alyssa', 16, 4.5, 1)") # inserts data into a table

all_students = [
    ('Jane', 17, 3.8, 0),
    ('John', 15, 3.2, 1),
    ('Joe', 16, 3.6, 1)
]
c.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", all_students) #data inside the list will appear in the (?,?,?)

# selects the data
c.execute("SELECT * FROM students")
print(c.fetchall())

conn.commit() # commit

conn.close() # closes the connection and makes the file