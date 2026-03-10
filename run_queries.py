import sqlite3

conn = sqlite3.connect("data/sample.db")
cur = conn.cursor()

print("=== Query 1: All students ===")
for row in cur.execute("SELECT * FROM students"):
    print(row)

print("\n=== Query 2: High scorers ===")
for row in cur.execute("SELECT * FROM students WHERE score >= 85"):
    print(row)

print("\n=== Query 3: Average by cohort ===")
for row in cur.execute("SELECT cohort, AVG(score) FROM students GROUP BY cohort"):
    print(row)

print("\n=== Query 4: Students + projects ===")
for row in cur.execute("""
SELECT students.name, projects.project
FROM students
JOIN projects ON students.id = projects.student_id
"""):
    print(row)

conn.close()