# import sqlite3
# import datetime
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
#         with self.ema:
#             self.ema.execute("""
#             INSERT INTO sheta (wallet)
#             VALUES (?)
#             """, (wallet))

#     def Money_take(self,wallet):
#         print("Вы выбрали положить деньги на счет.")
#         der=int(input("Выберите, сколько хотите положить: "))
#         print(f'вы успешно положили деньги вас счет состовляет {wallet+der}')
    
#     def credit(self,wallet):
#         print("Вы выбрали взять кредит.")
        










# # # Пример использования
# nachalo = Nachalo()
# nachalo.Reg()
# nachalo.Money_give()
# nachalo.Money_take()
# # nachalo.Money_give(1000)
# class Math:
#     def __init__(self,number1,number2):
#             self.number1=number1
#             self.number2=number2
#     def __add__(self):
#         print (self.number1-self.number2)
#     def __sub__(self):
#         print (self.number1+self.number2)
# nerd=Math(8,9)
# nerd.__add__()
# nerd.__sub__()
class  Constructor:
    def __init__(self , stroitsa):
        self.stroitsa=stroitsa
    def Build(self):
        while True:
            self.stroitsa>20
            self.stroitsa += 1
    def __str__(self , stroitsa):
        print(f"обьект компании Nurzaman plaza  завершен в высотой {self.stroitsa}")
ddd=Constructor(0)
ddd.__str__()
    
