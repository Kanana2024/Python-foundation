age = int(input("How old are you?"))
if age >= 68:
    print("You are old enough to retire")
    print("You are old enough to have an ID")
elif age < 65 and age >= 50:
    print("You are almost going to retire")
elif age <50 and age >= 40:
    print("You are still active")
elif age < 40 and age >=18:
    print("You are considered youthful")
else:
   print("You are still young")

marks = float(input("Enter your marks"))

if marks >= 80 and marks <=100:
    print("You have an A")
elif marks >=60 and marks <=79:
    print("You have a B")
elif marks >=50 and marks <=59:
    print("You have a C")
elif marks >=40 and marks <=49:
    print("You have a D")
elif marks >=0 and marks <=39:
    print("You have an E")
else:
    print("Enter valid marks")

temperature = float(input("Enter your temperature"))
if temperature >=30:
    print("Have a vest on")
elif temperature >=30 and temperature <=20:
    print("Put on a sweater")
elif temperature <20:
    print("Put on a jacket")


height = float(input("Enter your height in meters"))
weight = float(input("Enter your weight in kilograms"))
BMI = float(weight)/float(height*height)
print(BMI)
if BMI <18:
    print("You are underweight")
elif BMI <25 and BMI >18:
    print("You are normal")
elif BMI <30 and BMI >25:
    print("You are overweight")
elif BMI >30:
    print("You are obese")

