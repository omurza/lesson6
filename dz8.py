# import sqlite3
# class Bank:
#     def __init__(self, balance=0):
#         self.balance = balance
#     def deposit(self):
#         x = int(input("Введите сумму, которую хотите положить на счет-  "))
#         self.balance += x
#         conn = sqlite3.connect('bank.db')
#         c = conn.cursor()
#         c.execute('CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY, balance INTEGER)')
#         c.execute('DELETE FROM account')
#         c.execute('INSERT INTO account (balance) VALUES (?)', (self.balance,))
#         conn.commit()
#         conn.close()
#         print(f'Вы положили на счет-, {x}, . Ваш счет равняется-, {self.get_balance()}')
#     def snatie(self):
#         y = int(input("Введите сумму, которую хотите снять со счета- "))
#         if y <= self.balance:
#             self.balance = self.balance - y
#             conn = sqlite3.connect('bank.db')
#             c = conn.cursor()
#             c.execute('''CREATE TABLE IF NOT EXISTS account 
#                     (id INTEGER PRIMARY KEY,
#                      balance INTEGER)''')
#             c.execute('DELETE FROM account')
#             c.execute('INSERT INTO account (balance) VALUES (?)', (self.balance,))
#             conn.commit()
#             conn.close()
#             print(f"Операция прошла успешно: вы сняли,{y},  и ваш счет равняется, {self.get_balance()}")
#         else:
#             print("Транзакция невозможна, так как не хватает средств")
#     def load_balance(self):
#         conn = sqlite3.connect('bank.db')
#         c = conn.cursor()
#         c.execute('''CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY,
#                    balance INTEGER)''')
#         c.execute('SELECT balance FROM account')
#         r = c.fetchone()
#         conn.close()
#         return r[0] if r else None

#     def get_balance(self):
#         return self.balance

# nerd = Bank()
# nerd.balance = nerd.load_balance() if nerd.load_balance() != None else nerd.get_balance()
# nerd.deposit()
# nerd.snatie()
# import sqlite3
# class student:
#     def start():
#         co=sqlite3.connect('kurs.db')
#         cor = co.cursor()
#         cor.execute(""" CREATE IF NOT EXIST kurs.db,
#                     id INTEGER PRIMARY KEY.
#                     name TEXT,
#                     age INTEGER ,
#                     uroki  TEXT,        
# """)
#         name=(input("введите имя-"))
#         age=int(input("введите возраст-"))
#         uroki=(input("введите предметы-"))
#         cor.execute("""INSERT INTO kursi (name,age,uroki)     VALUES(?,?,?)""" (name,age,uroki))
#         cor.commit()
#         cor.close()
#     def start1():
#         co=sqlite3.connect('uroki.db')
#         cor = co.cursor()
#         cor.execute(""" CREATE IF NOT EXIST uroki.db,
#                     id INTEGER PRIMARY KEY.
#                     time INTEGER ,
#                     uroki  TEXT,        
# """)
#         name=(input("введите имя-"))
#         time=int(input("введите возраст-"))
#         uroki=(input("введите предметы-"))
#         cor.execute("""INSERT INTO kursi (name,time,uroki)     VALUES(?,?,?)""" (name,time,uroki))
#         cor.commit()
#         cor.close()




# class Student: 
#     def __init__(self,students,curs): 
#         self.students = students 
#         self.curs = curs 
#     def info(self): 
#         print(f"Студент-{self.students} курс-{self.curs}") 
# class Course: 
#     def __init__(self,cours, credit): 
#         self.cours = cours 
#         self.credit = credit 
#     def info(self): 
#         print(f"Курс-{self.cours} Кредиты-{self.credit}") 
#     def add_course(self): 
#         self.user = input("введите название курса: ") 
#         self.user + self.cours 
#         print("курс добавлен") 
#         self.credit + self.credit 
         
#         print(f"кредиты {self.credit}") 
# course = Course("backend",240) 
# course.info() 
# course.add_course() 
 
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
# class Library:
#     def __init__(self):
#         self.books = []
#     def add_book(self, book):
#         self.books.append(book)
#     def find_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 return book
#     def list_books(self):
#         if not self.books:
#             print("Библитека пуста.")
#         else:
#             for book in self.books:
#                 print(f"{book.title} - {book.author}, {book.year}")
# library = Library()
# book1 = Book("461 по фарингейтов", " рей бредбери /кстати очень интересная книга советую прочитать",1953 )
# book2 = Book("my fight", "adolf gitler", 1934)
# book3 = Book("вьвьвьвь", "это делал нурбек", 2024)
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# found_book = library.find_book("1984")
# if found_book:
#     print(f"Найдена книга: {found_book.title} - {found_book.author}, {found_book.year}")
# else:
#     print("Книга не найдена.")
#     print(" Все книги в библиотеке:")
# library.list_books()
# from math import pi
# class Verd:
#     def __init__(self,dlina,shirina,diametr):
#         self.dlina=dlina
#         self.shirina=shirina
#         self.diametr=diametr
#     pass
#     def parametr(self):
#         ff=self.dlina*self.shirina
#         print(f"ваш площядь равет {ff}")
#         f=self.dlina+self.shirina+self.dlina+self.shirina
#         print(f"ваш периметр равен {f}")
#     def diam(self):
#         gg= 3,14*self.diametr*2
#         print(f"ваша площядь круга равна-{gg}")
#         g=2*pi*self.diametr
#         print(f"ваш периметр круга равна-{g}")
# dd=Verd(110,20,1000000)
# dd.parametr()
# dd.diam()
import sqlite3
conn = sqlite3.connect('garage.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        make TEXT,
        model TEXT,
        year INTEGER)''')
def add_car(make, model, year):
    cursor.execute('INSERT INTO cars VALUES (?, ?, ?)', (make, model, year))
    conn.commit()
def remove_car(make, model):
    cursor.execute('DELETE FROM cars WHERE make = ? AND model = ?', (make, model))
    conn.commit()
def list_cars():
    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()
    if cars:
        for car in cars:
            print(f" {car[0]} {car[1]}")
    else:
            print("нету тут ничего")
add_car("Toyota", "Camry", 2020)
add_car("Honda", "Civic", 2019)
print("Cars in the garage:")
list_cars()
remove_car("Honda", "Civic")
list_cars()

