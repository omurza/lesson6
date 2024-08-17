class campucter:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    def __make_computations(self):
        cloz = self.__cpu + self.__memory
        vich = self.__cpu - self.__memory
        umnz = self.__cpu * self.__memory
        dell = self.__cpu / self.__memory 
        return (cloz, vich, umnz, dell)
    def cpu(self):
        return self.__cpu
    def memory(self):
        return self.__memory
    def info(self):
        computations = self.__make_computations()
        info_str = (
            f"CPU: {self.__cpu}\n"
            f"Memory: {self.__memory}\n"
            f"Сложение: {computations[0]}\n"
            f"Вычитание: {computations[1]}\n"
            f"Умножение: {computations[2]}\n"
            f"Деление: {computations[3]}\n")
        return info_str
class nout(campucter):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card
    def memory_card(self):
        return self.__memory_card
    def info(self):
        base_info = super().info()
        additional_info = (f"Карта памяти: {self.__memory_card}\n")
        return base_info + additional_info
comp = campucter(8, 4)
lap = nout(16, 8, '256GB')
print(comp.info())
print(lap.info())
print(f"CPU компьютера: {comp.cpu}")
print(f"Memory ноутбука: {lap.memory}")
print(f"Карта памяти ноутбука: {lap.memory_card}")
print(comp.info())
print(lap.info())
