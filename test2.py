def student(firstname,lastname,gender,age):
    print(firstname + '' + lastname + "is a", gender ,"who is", age ,"years old")
student("Natasha","Muthomi","female", 15)

class Student:
    student_name = "Natasha"
    marks = 90
print(Student.student_name)
print(Student.marks)
Student.student_name = "Linah"
Student.marks = 95
print(Student.student_name)
print(Student.marks)

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.area = length * width

v = Rectangle(20,20)
print(v.area)
class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.perimeter = float(22/7)*(radius*2)
        self.area = float(22/7)*(radius*radius)
a = Circle(37)
print(a.area)
print(a.perimeter)

class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit(self):
       deposit = int(input("Enter amount you would like to deposit"))
       balance = self.balance + deposit
       print(f"Dear {self.customer_name} you new balance is {balance}")
    def withdraw(self):
        withdraw = int(input("Enter amount you would like to withdraw"))
        balance = self.balance - withdraw
        print(f"Dear {self.customer_name} your new balance is {balance}")
obj4 = BankAccount(205674,5000000,"Third","Natasha")
obj4.deposit()
obj4.withdraw()


















