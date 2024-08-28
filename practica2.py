# # class  Car:
# #     def __init__(self,model,marka,color):
# #         self.model=model
# #         self.marka=marka
# #         self.color=color
# #     def info(self):
# #         print(f'ваша машина {self.model},ваша марка {self.marka} , ваш цвет машины {self.color}')
# # # car1=Car ('e8' , 'bmw' , 'green')
# # # car1.info()

# # class Bexa(Car):
# #     def __init__(self, model, marka, color, motor):
# #         super().__init__(model, marka, color)
# #         self.motor=motor
# #     def information(self):
# #         print(f'ваша машина {self.model},ваша марка {self.marka} , ваш цвет машины {self.color}, ваша мощьность мотора {self.motor}')
# # # car2=Bexa('e8' , 'bmw' , 'green' ,' 2000 лошадиных сил')
# # # car2.information()
# # class track(Bexa):
# #     def __init__(self, model, marka, color, motor, kuzov,ves):
# #         super().__init__(model, marka, color, motor)
# #         self.kuzov=kuzov
# #         self.ves=ves
# #     def dan(self):
# #         print(f'ваша машина {self.model},ваша марка {self.marka} , ваш цвет машины {self.color}, ваша мощьность мотора {self.motor} , кузов вашей машини {self.kuzov} вес вашей машини {self.ves}')
# # car3=track('e8' , 'bmw' , 'green' ,' 2000 лошадиных сил', 'плоский' ,' вес вашей машины 1,5 тонны')
# # car3.dan()
# # class People:
# #     def __init__(self , name , age , hight , weight):
# #         self.name=input("введите имя")
# #         self.age=int(input("введите имя"))
# #         self.hight=int(input("введите имя"))
# #         self.weight=int(input("введите имя"))
# #     def info(self):
# #         print('имя-{self.name} возраст-{self.age}')
# # result = People('?','?','?','?')
# # result.info()
# # class Student:
# #     def __init__(self,name ,  age , ):
# #         self.name=name
# #         self.age=age
# #         self.grades=[]

# #     def info1(self):
# #         grade=int(input("введите ваши оценки:")) 
# #         self.grades.append(grade)

# #     def srednac(self):
# #         return sum(self.grades) / len(self.grades) if self.grades else 0
    
# #     def info(self):
# #         print(f'ваше имя-{self.name},ваш возраст-{self.age},ваш средняя арифметическая оценка- {self.srednac():.2f}')

# # nerd=Student('adolf gitler' , 34 )
# # nerd.info1()
# # nerd.info()
# # nerd.srednac()
# # for i in range(3):
# #     nerd.info1()

# # class Student:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         self.grades = []

# #     def add_grade(self):
# #         grade = int(input("Введите оценку: "))
# #         self.grades.append(grade)

# #     def average_grade(self):
# #         return sum(self.grades) / len(self.grades) if self.grades else 0

# #     def display_info(self):
# #         print(f"Имя: {self.name}")
# #         print(f"Возраст: {self.age}")
# #         print(f"Средняя оценка: {self.average_grade():.2f}")

# # # Пример использования
# # student = Student("Алиса", 20)

# # # Добавление оценок
# # for _ in range(3):
# #     student.add_grade()

# # # Отображение информации о студенте
# # student.display_info()

# # import random 
# # class 

# import sqlite3

# class Nachalo:
#     def __init__(self, db_evrey='sheta'):
#         self.ema = sqlite3.connect(db_evrey)
#         self.Create()

#     def Create(self):
#         with self.ema:
#             self.ema.execute("""
#             CREATE TABLE IF NOT EXISTS sheta (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 birth_year INTEGER,
#                 email VARCHAR(100),
#                 wallet INTEGER DEFAULT NULL
#             )
#             """)

#     def Reg(self):
#         name = input("Введите ФИО: ")
#         birth_year = int(input("Введите возраст: "))
#         if birth_year < 18:
#             print("Регистрация невозможна, так как вам нет 18 лет.")
#             return
#         email = input("Введите email: ")
#         if '@' in email:
#             print("Email добавлен.")
#         else:
#             print("Вы не добавили email.")
#             return

#         with self.ema:
#             self.ema.execute("""
#             INSERT INTO sheta (name, birth_year, email)
#             VALUES (?, ?, ?)
#             """, (name, birth_year, email))

#     def Money_give(self, wallet):
#         print("Вы выбрали выдачу наличных.")
#         abv = int(input("Выберите, сколько хотите снять: "))
#         if wallet >= abv:
#             wallet -= abv
#             print(f"Остаток на счете: {wallet} руб.")
#         else:
#             print("Недостаточно средств на счете.")

# # Пример использования
# nachalo = Nachalo()
# nachalo.Reg()
# nachalo.Money_give(1000)





















class Constructor:
    def __init__(self, stroitsa):
        self.stroitsa = stroitsa

    def Build(self):
        while self.stroitsa < 20:
            self.stroitsa += 1

    def __str__(self):
        return f"Объект компании Nurzaman plaza завершен на высоте {self.stroitsa} этажей"

ddd = Constructor(0)
ddd.Build()
print(ddd)


















































































































































































































