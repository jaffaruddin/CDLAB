# sqlite3 database
import sqlite3
conn = sqlite3.connect('StudentInfo')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Student')
cur.execute('CREATE TABLE Student(name TEXT, rno INTEGER)')
cur.execute('INSERT INTO Student (name, rno) VALUES (?, ?)', ('MAHESH', 30))
cur.execute('INSERT INTO Student (name, rno) VALUES (?, ?)', ('RAHUL', 42))
cur.execute('SELECT * FROM Student')
print(cur.fetchall())

conn.close()

-> o/p: [('MAHESH', 30), ('RAHUL', 42)]
