my_dictionary = {
    "Name": "Natasha",
    "Gender": "Female",
    "Age": 18,
    "Marital status": "Single",
}
print(my_dictionary)
print(my_dictionary["Marital status"])
print(my_dictionary["Name"])
print(my_dictionary.get("Gender"))
my_dictionary["Marital status"] = "Married"
print(my_dictionary)
my_dictionary["Age"] = 24
print(my_dictionary)
my_dictionary["Location"] = "Nairobi"
print(my_dictionary)
my_dictionary["Salary"] = 1000000
print(my_dictionary)

my_dictionary2 = my_dictionary.copy()
print(my_dictionary2)
print(len(my_dictionary))
my_dictionary.pop("Marital status")
print(my_dictionary)
my_dictionary.pop("Age")
print(my_dictionary)
del my_dictionary["Gender"]
print(my_dictionary)
my_dictionary.clear()
print(my_dictionary)
del my_dictionary
print(my_dictionary2)


car = {
    "Name": "Land Cruiser",
    "Model": "veight",
    "Year of manufacture": "2025",
    "Origin": "Germany",
    "Color": "Black"
}
print(car)
car["Designer"] = "Vincent"
print(car)
car["Origin"] = "Japan"
print(car)
car.pop("Model")
print(car)
del car["Color"]
print(car)