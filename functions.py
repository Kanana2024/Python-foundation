print()


def my_function():
    print('This is my first function')
    print('This is my first function')
    print('This is my first function')
my_function()
def karibu(name):
    print(name)
    print(name)
    print(name)
karibu('Naomi')
karibu('Ann')
karibu('Kim')

def num(nambari):
    print(nambari)
    print(nambari)
num(56)


def salutation(first_name):
    print('Hi '+ first_name + ' Good morning')
salutation('Esther')

def miaka(age):
    print('Hello, you are ' +str(age) + ' years old')
miaka(18)

def my_name(first_name, last_name):
    print(first_name + '' + last_name + " this is the student")
my_name('Naomi', 'Wachuka')



def sentence(first_name, last_name, age):
    print(first_name + '' + last_name + 'is' + str(age) + ' years old')
sentence('Naomi', 'Wachuka', 34)


def employees(first_name, age):
 if age >= 20:
    print(first_name + 'you are' + str(age) +'years old')
 elif age<20 and age>=15:
    print(first_name + 'you are' + str(age) +'years old')
 elif age<15 and age>=10:
    print(first_name + 'you are' + str(age) +'years old')
 else:
    print(first_name + 'you are' + str(age))
employees('John',23)


def age_calculator(age):
    new_age = age +10
    return new_age
print(age_calculator(18))

def marks_calculator(*subjects):
    total_marks = sum(subjects)
    return total_marks
print(marks_calculator(35,78,52))
print(marks_calculator(54,72,94))
print(marks_calculator(34,56))


def exam(name,pre,post):
    total = name + 'your total is '+str(pre+post)
    return total
print(exam('Ann', 78,67))


def work(location,age):
    if age >60:
        print("Posted to Kisumu")
    elif age<=60 and age>=50:
        print("Posted to Nakuru")
    elif age<=40 and age>=30:
        print("Posted to Mombasa")
    else:
        print("Posted to Nairobi")
work()


def country(nchi = "Kenya"):
    return nchi
print(country("Tanzania"))


