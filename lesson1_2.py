# '''OOP'''
# class Car():
#     def __init__(self, model , color):
        
#     # cars=("bmw","mersedes","honda","audi")
#         self.model= model 
#         self.color= color 
#         self.ton=10
#         self.is_start= False
        
#     def info(self):
#             print(f" модель- {self.model } цвет-{self.color}")
#     def start(self):
#         if self.ton > 0:
#              self.is_start=True
#              print("pfdt")
#         else:
#              print("dm")
#     def stop(self):
#          self.is_start=False
#          print("dj")
#     def drive(self):
#         if  self.is_start ==False:
#             print("не поедет машина")c
#         else:
#             print("cnn")
# bmw= drive('moscow')
# bmw=Car('m8', ' bmw')
# # bmw.info()
# # bmw.start()
# bmw.stop()

# def info(self):
#         print(f" расоя}")
#         if self.toplivo >0 :
#             print("фиг тебе не поездка")
        
# class book():
#     def __init__(self , aughtor , book_name , year):
#         self.aughtor=aughtor
#         self.book_name=book_name
#         self.year=year
#     def info(self):
#             print(f" автор-'{self.aughtor} 'название книги- ' {self.book_name} 'год выпуска-' {self.year}")
# book1=book('adolf gitler', ' my fight', '1934')
# book1.info()


# class Car: #шаблон или же чертеж 
#     def __init__(self, model, marka, color):
#         'Атрибут объекта'
#         self.model = model
#         self.marka = marka
#         self.color = color
#         'Атрибут класса'
#         self.bak = 10
#         self.is_start = False
        
#     def info(self):
#         print(f'Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}')
        
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print(f'Машина {self.marka} - {self.model} заведена')
#         else:
#             print(f'Машина {self.marka} - {self.model} нет топлива')
            
#     def stop(self):
#         self.is_start = False
#         print(f'Машина {self.marka} - {self.model} заглушено')
        
        
        
        
# bmw = Car('m5 f90', 'BMW', 'black')
# bmw.info()
# bmw.start()
# bmw.stop()
