"CRUD "
from database import Database
class Aughtor:
    def __init__(self,name, nerd):
        self.name=name
        self.nerd=nerd
    def __str__(self):
        return f' автор {self.name}, дата рождения {self.nerd}'
aughtor=Aughtor("aslan", 2008)
# print(aughtor)
class Book:
    def __init__(self, title , aug , public2):
        self.title=title
        self.aug=aug
        self.public2=public2
    def __str__(self):
        return f'название книги {self.title}, автор{self.aug}, год публикации{self.public2}'
class Bib:
    def __init__(self , db : Database):
        self.db=db
        if not self.db.get_aughtor(aughtor.name):
            self.db.add_aughtor(aughtor.name,aughtor.nerd)
    def add_book(self):
        if aughtor is None :
