# import sqlite3

# class Database:
#     def __init__(self , db_name='library.db'):
#         self.conn=sqlite3.connect(db_name)
#         self.create_tables()


#     def create_tables(self):
#         with self.conn:
#             self.conn.execute("""CREATE TABLE IF NOT EXIST aughors_adolf(
#                             id INTEGER PRIMARY KEY,
#                             name TEXT ,
#                             data_roz INTEGER,
#             )
# """)
#             self.conn.execute("""CREATE TABLE IF NOT EXIST books(
#             id INTEGER PRIMARY KEY,
#             title TEXT,
#             aughtor_id INTEGER,
#             FOREIGN KEY (aughtor_id) REFERENCES aughtors (id)
#             )
# """)


#     def add_aughtor(self,name,data_roz):
#         with self.conn:
#             self.conn.execute('INSERT INTO aughtors_adolf(name,data_roz)VALUES(?,?)',
#             (name,data_roz))
    
#     def get_aughtor(self,name):
#         cursor=self.conn.cursor()
#         cursor.execute('SELECT id,name,data_roz FROM augtors_adolf WHERE name=?')
#         (name)
#         return cursor.fetchone()
#     def add_book(self,title,audhtor_id,public):
#         with self.conn:
#             self.conn.execute('INSERT INTO books (title,aughtor_id,public) VALUES(?,?,?)'   
#         (title , audhtor_id , public)


#             )

#     def remove(self,title):
#         with self.conn:
#             self.conn.execute('DELETE FROM books WHERE title=?',(title),)
#     def find(self,aughtor_name):
#         cursor=self.conn.cursor()
#         cursor.execute('''SELECT books.title, augtor_name,books.public
#                         FROM books
#                        JOIN aughtor ON books.aughtor_id=aughtor_id
#                        WHERE aughtor.name=?
# ''',(aughtor_name))
#         return cursor.fetchall()
#     def list_b(self):
#         cursor=self.conn.cursor()
#         cursor.execute('''
        
# SELECT book.title, aughtors.name,books.public
#                        FROM books
#                        JOIN aughtors
#                        on books_aughtors_id = aughtors_id''')
    


ef Plachu(self):
        aaa=input("""\n выберите номер действия 1-регистрация за 5 секунд 2-денги давай ааааа да у меня сил дохуя 
                        3-кредит хочащ 4-пополнить счет 5-посмотреть ссчет""")
        if aaa==1:
            print("вы выбрали регистрацию")
            print(Reg())
        elif aaa==2:
            print("вы выбрали ДЕНЬГИ ДАВАЙ")
        elif aaa==3:
            print("кредитик по 12 процентов день но в подарок ручка")
        elif aaa==4:
            print("вы выбрали пополниь счет")
        elif aaa==5:
            print("вы выбрали посмотреть счет")
        else:
            print("такого не было не было")
    def Reg():
        name=input("введите имя-")
        birth_year=int(input("введите возраст-"))
        if birth_year< 18:
            print(" регистрация не возможно так как нет 18 лет")
        email=input("введите имеил")
        if '@' in email:
            print("имеил добавлен")
        else :
            print("вы не добавили имеил")

    def Money_give():
        pass
    def Credit():
        pass
    def Popolnit():
        pass
    def money_look():
        pass





















































































































































































