class Appliance :
    def nerd(self):
        pass
    def turn_of(self):
        pass
    def turn_on(self):
        pass
    def use(self):
        pass
    def repair(self):
        pass

class Stirca(Appliance):
    def use(self):
        return ' стиралка стирает'
    def repair(self):
        return ' стиралка в ремонте почему карманы не проверили идиоты'
    
class Micro(Appliance):
    def use(self):
        return ' микраволновка разогревает еду'
    def repair(self):
        return ' микроволновка в ремонте почему вилку оставили идиоты'
    
class Xolodoc(Appliance):
    def use(self):
        return ' холодильник (сокровищнеца) охлождает еду'
    def repair(self):
        return ' холодильник в ремонте почему дверь открытой оставили идиоты'
    
stirca = Stirca()

print(stirca.use())
print(stirca.repair())

tirca = Micro()

print(tirca.use())
print(tirca.repair())

irca = Xolodoc()

print(irca.use())
print(irca.repair())














