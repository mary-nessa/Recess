# Tuples are used to store items in a single variable
# they are ordered and unchangeable

phones = ("nokia", "Iphone", "tecno")
print(phones)

# allow diplicate values
# find their length using the len() method
phones = ("nokia", "Iphone", "tecno", "nokia", "Iphone", "tecno", "tecno")
print(len(phones))

# tuple holding different datatypes
tuple1 = ("sweetpotatoes", "rice")
tuple2 = (100, 200, 300, 500)
# print(type(tuple1), type(tuple2))

# Exercise accessing a tuple
print(tuple1[0])

# Adding items to the tuple
phones = ("Nokia", "tecno")
z = list(phones)
z.append("Nokia")
phones = tuple(z)
print(phones)

# Adding tuples together
laptops = ("Dell XPS", "HP Spectre", "Lenovo ThinkPad")
new_laptops=("MacBook Pro", "Asus ZenBook")
laptops = laptops + new_laptops
laptops += new_laptops
print(laptops)
print(new_laptops)

# for loops to loop through tuples
for t in laptops:
    print(t)
