import sqlite3

conn = sqlite3.connect("data/sample.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE students (
id INTEGER PRIMARY KEY,
name TEXT,
cohort TEXT,
score INTEGER
)
""")

cur.execute("""
CREATE TABLE projects (
id INTEGER PRIMARY KEY,
student_id INTEGER,
project TEXT
)
""")

students = [
(1,"Alice","AI-2025",95),
(2,"Bob","AI-2025",88),
(3,"Charlie","AI-2024",72),
(4,"Diana","AI-2024",90)
]

projects = [
(1,1,"Chatbot"),
(2,2,"Vision Model"),
(3,3,"Data Pipeline"),
(4,4,"Recommendation System")
]

cur.executemany("INSERT INTO students VALUES (?,?,?,?)", students)
cur.executemany("INSERT INTO projects VALUES (?,?,?)", projects)

conn.commit()
conn.close()

print("Database created successfully")