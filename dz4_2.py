class Vehicle:
    def move1(self,move, top1):
        return(f'обьект-{move} движется')
    pass
    
    def fuel(self,top1):
        return(f'обьект-{top1} топливо')
           
class Car(Vehicle):
    def move1(self,move):
        return(f'машина-{move}  по дороге')
    
    def fuel(self,top1):
        return(f'обьект-{top1} дизель')
    

class Boat(Vehicle):
    def move1(self,move):
        return(f'лодка-{move}  по воде')
    
    def fuel(self,top1):
        return(f'обьект машина-{top1} бензин')
    


class bike(Vehicle):
    def move1(self,move):
        return(f'велосипед-{move}  по тратуару')
    
    def fuel(self,top1):
        return(f'обьект велосипед-{top1} силу ног')
nerd={bike(),Boat(),Car()}
for oop in nerd:
    print(oop.move1('движется'))
for oop1 in nerd:
    print(oop1.fuel('расходует'))
