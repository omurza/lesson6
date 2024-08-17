# class Fruict():
#     def __init__(self , name , color , weight):
#         self.name=name
#         self.color=color
#         self.weight=weight
#     def info(self):
#             print(f" фрукт-'{self.name} 'цвет- ' {self.color} 'вес-' {self.weight}")
# book1=Fruict('апельсин', ' оранжевый', '234 грамма')
# book1.info()

class Book():
    def __init__(self , aughtor , book_name , year , check_pages):
        self.aughtor=aughtor
        self.book_name=book_name
        self.year=year
        self.check_pages=check_pages

    def info(self):
            print(f" автор-'{self.aughtor} 'название книги- ' {self.book_name} 'год выпуска-' {self.year} страницы - {self.check_pages}"  )

    def title(self):
        if  self.check_pages < 100:
            print('тонкая книга')
        elif self.check_pages <= 300:
            print('средняя книга')
        else:
             print('большая книга')

    
book1=Book('adolf gitler', ' my fight', '1934', 150)
book1.info()
book1.title()