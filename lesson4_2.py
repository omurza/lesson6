# "полиморфизм"

# # num1=1
# # num2=2
# # print(num1+num2)
# # print(len("oop prog"))
# class Cat:
#     def __init__(self , name , pref):
#         self.name=name
#         self.pref= pref
#     def info(self):
#         print(f'я кот-{self.name}, мне {self.pref} года')
#     def make_s(self):
#         print('мяу')
# class Dog:
#     def __init__(self , name , pref):
#         self.name=name
#         self.pref= pref

#     def info(self , color):
#         print(f'я собака-{self.name}, мне {self.pref} года цвет {color}')

#     def make_s(self):
#         print('гав')

# cat = Cat('василий',23 )
# dog = Dog('армянин',3)
# # Cat.info()
# # Dog.info()
# for animal in (cat , dog):
#     animal.make_s()
#     dog.info('черный')
#     animal.make_s()
# class Oplata:
#     def pay(self , amount):
#         pass
# class Credit(Oplata):
#     def pay(self,amount):
#         return f'сумма {amount} оплачена кредиткой'
# class Paypal(Oplata):
#     def pay(self,amount):
#         return f'сумма {amount} оплачена paypal'
# class Bank(Oplata):
#     def pay(self,amount):
#         return f'сумма {amount} оплачена банком '   
    
# oplatocki={Credit(), Paypal() ,Bank()}
# for op in oplatocki:
#     print(op.pay(100))






























































































































