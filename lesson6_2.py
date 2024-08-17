# "база данных-ячейка" 
# "субд-система управления базы данных" 
# "crud- create , read,update,delete"
# import sqlite3
# conect=sqlite3.connect("nerd.db")
# cursor=conect.cursor()

# cursor.execute("""
#         CREATE TABLE IF NOT EXISTS nerd.pd(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             full_name VARCHAR(30) NOT NULL,
#             age INT DEFAULT NULL,
#             direction  TEXT,
#             is_have BOOLIAN NOT NULL DEFAULT FALSE,
#             rating  DOUBLE(4,2) DEFAULT(0,0),
#             data_birth DATE
#                )
# """)

# def registr():
#     full_name=input('введите имя:')
#     age=int(input('введите возраст:'))
#     direction=input('введите направление:')
#     is_have=bool(input('введите наличие ноута:'))
#     rating=float(input('введите свой рейтинг:'))
#     data_birth=input('введите дату рождения:')


# registr()
# "БД - База данных"
# "СУБД - Система управления базой данных"
# "CRUD - CREREATE, READE, UPDATE, DELETE"

# import sqlite3

# connect = sqlite3.connect("geeks.db")
# cursor = connect.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS geeks(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         full_name VARCHAR (30) NOT NULL,
#         age INT DEFAULT NULL,
#         direction TEXT,
#         is_have BOOLEAN NOT NULL DEFAULT FALSE,
#         rating DOUBLE (4,2) DEFAULT (0.0),
#         birth_date DATE
#     )               
# """)

# def register():
#     full_name = input("Введите ФИО: ")
#     age = int(input("Введите возраст: "))
#     direction = input("Введите направление: ")
#     is_have = bool(input("Наличие ноутбука: "))
#     rating = float(input("Введите свой рейтинг: "))
#     birth_date = input("Введите дату рождения")


# #     cursor.execute(f''' INSERT INTO geeks
# #                 (full_name , age , direction , is_have , rating , bitth_date)    
# #                 VALUES ('{full_name}' ,{age} '{direction}, {is_have} ,{rating} ,{birth_date}')
# #                    ''')

# #     connect.commit()
# # register()
#     cursor.execute("""  INSERT INTO geeks
#                 (full_name , age , direction , is_have , rating , bitth_date)
#                  VALUES (?,?,?,?,?,?) """ ,(full_name , age , direction , is_have , rating , birth_date ))
#     connect.commit()
# register()

# def all_student():
#     cursor.execute("""SELECT * FROM geeks""")
#     students=cursor.fetchall()
#     print(students)
# # register()
# all_student()



"БД - База данных"
"СУБД - Система управления базой данных"
"CRUD - CREREATE, READE, UPDATE, DELETE"

import sqlite3

connect = sqlite3.connect("geeks.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS geeks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (30) NOT NULL,
        age INT DEFAULT NULL,
        direction TEXT,
        is_have BOOLEAN NOT NULL DEFAULT FALSE,
        rating DOUBLE (4,2) DEFAULT (0.0),
        birth_date DATE
    )               
""")

def register():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите возраст: "))
    direction = input("Введите направление: ")
    is_have = bool(input("Наличие ноутбука: "))
    rating = float(input("Введите свой рейтинг: "))
    birth_date = input("Введите дату рождения: ")

    # cursor.execute(f"""INSERT INTO geeks
    #                (full_name, age, direction, is_have, rating, birth_date)
    #                VALUES ('{full_name}', {age}, '{direction}', {is_have}, {rating}, '{birth_date}')""")
    
    # connect.commit()
    cursor.execute(""" INSERT INTO geeks 
                   (full_name, age, direction, is_have, rating, birth_date)
                   VALUES (?, ?, ?, ?, ?, ?)""", (full_name, age, direction, is_have, rating, birth_date))
    connect.commit()
register()
















































































































