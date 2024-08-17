class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def info(self):
        married_status = "Женат" if self.is_married else "Холостяк"
        print(f'Имя: {self.full_name}, Возраст: {self.age}, Женат либо холостяк: {married_status}')


class Teacher(Person):
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience
        self.salary = self.calculate_salary()

    def calculate_salary(self):
        bonus = (self.experience // 3) * 3000
        return bonus

    def info1(self):
        married_status = "Женат" if self.is_married else "Холостяк"
        print(f'Имя: {self.full_name}, Возраст: {self.age}, Женат либо холостяк: {married_status}, Опыт: {self.experience} лет, Зарплата: {self.salary}')



experience = int(input("Введите сколько лет вы проработали: "))
hahah = Teacher('Анатолий Иванович', 27, True, experience)
hahah.info1()
