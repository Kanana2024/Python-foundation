class Employees:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Receptionist(Employees):
    def __init__(self,name, salary, gender):
        super().__init__(name, salary)
        self.gender = gender
class Front_end_developer(Employees):
    def __init__(self,name,salary,programming):
        super().__init__(name,salary)
        self.programming = programming


Receptionist1 = Receptionist("Susan", 300000,"Female")
Employee1= Employees("Linah",700000)
print(Receptionist1.name)
print(Employee1.name)