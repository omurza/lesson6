# class Fruict():
#     def __init__(self , name , color , weight):
#         self.name=name
#         self.color=color
#         self.weight=weight
#     def info(self):
#             print(f" фрукт-'{self.name} 'цвет- ' {self.color} 'вес-' {self.weight}")
# book1=Fruict('апельсин', ' оранжевый', '234 грамма')
# book1.info()
import sqlite3
class Book():
    
    def __init__(self , aughtor , book_name , year , check_pages):
        self.aughtor=aughtor
        self.book_name=book_name
        self.year=year
        self.check_pages=check_pages

    
        connect = sqlite3.connect("test.db")
        cursor = connect.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR (30) NOT NULL,
                year INT DEFAULT NULL,
                book TEXT,
                title INT DEFAULT NULL
            )               
        """)
        connect = sqlite3.connect("test.db")
        cursor = connect.cursor()
        name = input("Введите ФИО: ")
        year = int(input("Введите возраст произведения: "))
        book=input("Введите название произведения: ")
        title=int(input("Введите колво стр: "))
        cursor.execute("""INSERT  INTO test (name,year,book,title) VALUES(?,?,?,?)""" 
                       
          , (name,year,book,title)
          
          )
        connect.commit()
        connect.close()
    def info(self):
            print(f" автор-'{self.aughtor} 'название книги- ' {self.book_name} 'год выпуска-' {self.year} страницы - {self.check_pages}"  )
    def create():

    
book1=Book
book1.info()
book1.