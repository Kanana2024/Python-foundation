class Person:
    name = "John"
    age = 18
    gender = "Female"
    marital_status = "Married"
print(Person.name)
print(Person.age)
print(Person.gender)
print(Person.marital_status)
Person.age = 20
print(Person.age)

class Employees:
    firstName = "John"
    lastName = "Muthomi"
    Salary = 6000000
    gender = "Male"
    age = 35
print(f"{Employees.firstName} {Employees.lastName} your age is {Employees.age} and you earn a salary of {Employees.Salary} and your gender os {Employees.gender}")
print(f"{Employees.lastName} you are a {Employees.gender} who earns {Employees.Salary}")
print(f"{Employees.firstName} is a {Employees.gender} of age {Employees.age}")

class Parent:
    firstName = "Esther"
    lastName = "Githuku"
parent1 = Parent()
print(parent1.firstName)


class Parent:
    def __init__(self,firstName, lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
Parent1 = Parent("John", "Kiprop", 35)
Parent2 = Parent("Gerald", "Kamau", 50)
Parent3 = Parent("Stacy", "Juma", 31)
print(Parent1.firstName)
print(Parent2.firstName)
print(Parent3.firstName)
print(Parent1.lastName)
print(Parent2.lastName)
print(Parent3.lastName)


class Cars:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
Car1 = Cars("Ford", "Ranger", 2000)
Car2 = Cars("Toyota", "Axis", 2014)
Car3 = Cars("Nissan","Sunny", 1999)
print(Car1.make)
print(Car2.make)
print(Car3.make)
print(f"My car model is {Car1.make} {Car1.model} manufactured in the year {Car1.year}")
print(f"{Car1.make}, {Car2.make}, {Car3.make} are all manufactured in the year {Car3.year}")

class Students:
    def __init__(self,name,grade,location):
        self.name = name
        self.grade = grade
        self.location = location
Student1 = Students("Angela","Seven","Nairobi")
Student2 = Students("Lisa", "Eight", "Mombasa")
print(f"{Student1.name} who is in grade {Student1.grade} lives in {Student1.location}."
      f"{Student2.name} who is in grade {Student2.grade} lives in {Student2.location}")

class Magari:
    def __init__(self,make,model,price,year):
        self.make = make
        self.model = model
        self.price = price
        self.year = year
    def describe(self):
        print(f"My favourite car is {self.make} and it is a make of {self.model} and it costs {self.price}")
obj1 = Magari("Ford","Ranger", 200000, 1999)
obj2 = Magari("Toyota","Axis",500000,2005)
obj3 = Magari("Nissan", "Sunny", 900000,2009)
print(obj1.describe())
print(obj2.describe())

class Person:
    def __init__(self,firstname,lastname,gender,age):
        self.firstname = firstname
        self.lastname =lastname
        self.gender = gender
        self.age = age
    def fullname(self):
        print(f"{self.firstname} {self.lastname}")
    def display_age(self):
        print(self.age)
    def increment_age(self):
        self.age +=10
    def display_gender(self):
        print(f"{self.gender}")
    def display_lastname(self):
        print(f"{self.lastname}")
obj1 = Person("Ann","Kagure","Female",36)
obj2 = Person("Timothy","Muchiri","Male",23)
print(obj1.fullname())
print(obj1.display_age())
print(obj1.display_gender())
print(obj1.display_lastname())
obj1.increment_age()
print(obj1.age)


class  Athletes:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def fullname(self):
        print(f"{self.fname} {self.lname}")
obj5 = Athletes("Natasha", "Kanana")
print(obj5.fullname())










