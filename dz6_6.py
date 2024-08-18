import sqlite3
import datetime
def baza():
    connect = sqlite3.connect("nurbek.db")
    cursor = connect.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            age INTEGER,
            grade TEXT NOT NULL,
            date DATE DEFAULT (DATE('now'))
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL,
            teacher_name TEXT NOT NULL
        )
    """)
    connect.commit()
    connect.close()
def rigistracia():
    connect = sqlite3.connect("nurbek.db")
    cursor = connect.cursor()
    full_name = input("Введите ФИО: ")
    age = int(input("Введите возраст студента: "))
    grade = input("Введите класс студента: ")
    cursor.execute("""
        INSERT INTO students (full_name , age , grade ) 
        VALUES (?, ?, ?)
    """, (full_name , age, grade ))
    connect.commit()
    connect.close()
    print("Студент добавлен.")
def urokci():
    connect = sqlite3.connect("nurbek.db")
    cursor = connect.cursor()
    subject_name = input("Введите название предмета: ")
    teacher_name = input("Введите имя преподавтеля: ")
    cursor.execute("""
        INSERT INTO subjects (subject_name, teacher_name) 
        VALUES (?, ?)
    """, (subject_name, teacher_name))
    connect.commit()
    connect.close()
    print("Предмет добавленн.")
def uchenick():
    connect = sqlite3.connect("nurbek.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)
    connect.close()
def Uroki():
    connect = sqlite3.connect("nurbek.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()
    for subject in subjects:
        print(subject)
    connect.close()
def ggg(grade):
    connect = sqlite3.connect("nurbek.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM students WHERE grade = ?", (grade,))
    students = cursor.fetchall()
    for student in students:
        print(student)
    connect.close()
def FFF(student_id, new_age):
    connect = sqlite3.connect("nurbek.db")
    cursor = connect.cursor()
    cursor.execute("""
        UPDATE students 
        SET age = ? 
        WHERE id = ?
    """, (new_age, student_id))
    connect.commit()
    connect.close()
    print("Возраст студента обновлен.")
def dell(student_id):
    connect = sqlite3.connect("nurbek.db")
    cursor = connect.cursor()
    
    cursor.execute("""
        DELETE FROM students 
        WHERE id = ?
    """, (student_id,))
    
    connect.commit()
    connect.close()
    print("Студент удален.")
baza()
rigistracia()
urokci()
uchenick()
Uroki()
ggg('10A')
# FFF(1, 20)
# dell(1)

