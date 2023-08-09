# Creating a list of laptops
laptops = ["Dell XPS", "HP Spectre", "Lenovo ThinkPad"]

# Accessing elements of a list
for laptop in laptops:
    print(laptop)

# Length of a list
length = len(laptops)
print(length)

# Adding items to a list
laptops.append("MacBook Pro")
laptops.append("Asus ZenBook")

print(laptops)

# Adding two lists together
additional_laptops = ["Surface Laptop", "Acer Swift"]
combined_laptops = laptops + additional_laptops

print(combined_laptops)

# Data type of a list
print(type(laptops))
