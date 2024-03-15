my_set = {122,133,144,155,166,177}
print(my_set)
my_set.add(199)
print(my_set)
my_set.update([111,222,333,444,555,666])
print(my_set)
my_set2 = my_set.copy()
print(my_set2)
print(len(my_set))
my_set.discard(111)
print(my_set)
my_set.clear()
print(my_set)
del my_set
print(my_set2)
print(max(my_set2))
print(min(my_set2))
print(sum(my_set2))
print(sum(my_set2)/len(my_set2))


names = {"John", "Mary", "Ann", "Naomi"}
print(names)
if "Mary" in names:
    print("Student is present in the school system")
else:
    print("Student is not present in the school system")

parents = {"Ivan", "Kim", "Angela", "Kevin"}
print(parents)
one_value = "Kim"
if one_value in parents:
    output = one_value
    print(output)


my_set3 = {23,56.0,90,87.4,95}
print(my_set3)
if 90 in my_set3:
    print("Value is present in the set" )
else:
    print("Value is not present in the set")
