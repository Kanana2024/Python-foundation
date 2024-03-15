a = "hello world"
print(a)
list = [100,22,77,88,11,99]
print(list)
list.sort()
print(list)
list.reverse()
print(list)

set = {11,22,33}
print(set)


s = 'STUDENT'
print(s)
s.lower()
print(s)

marks = float(input('Enter your marks'))
if marks>=80 and marks<=100:
    print("You have scored an A")
elif marks>=76 and marks<=80:
    print("You have scored an A-")
elif marks>=70 and marks<=76:
    print("You have scored a B+")
else:
    print("You have scored a grade below B+")

class Rectangle:
  def __init__(self,length,width):
      self.length = length
      self.width = width
      self.area = length * width
r = Rectangle(60,40)
print(r.area)

mlist = [20,78,99]
print(mlist)
mlist.extend([10,20,40])
print(mlist)
mlist.sort()
print(mlist)
mlist.count(20)
print(mlist)
mlist.reverse()
print(mlist)

class Paypalaccount:
    def __init__(self,account_no,customer_name,balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance




