#Dictionaries specified by dict
car = {
    'name':'Spacio',
    'model':'2017 model',
    'milage':110
}

#printing dictionary
print(car)

print(len(car)) #length of dictionary
print(type(car)) #specify data type

#How to access the dictioanry items
x = car['milage']

y = car.get('model')
print (x, y)



#Exercise1 Accessing values using the values()
# Accessing values using values() method
car_values = car.values()

# Printing the values
for value in car_values:
    print(value)
    
    

#Exercise2 checking if a key exists
# Checking if the key 'name' exists
if 'name' in car:
    print("The key 'name' exists in the dictionary.")
else:
    print("The key 'name' does not exist in the dictionary.")
    
     
#Exercise3 changing items and updating 
# Changing the value of the 'mileage' key
car['mileage'] = 120
car.update({"model":"2019"}) #can also use the update function

# Printing the updated dictionary
print(car)



#Exercise4 Adding and removing items
# Adding a new key-value pair
car['color'] = 'blue'

# Removing a specific key-value pair using del
del car['mileage']

# Printing the dictionary after deleting the key-value pair
print(car)

# Clearing all items from the dictionary using clear()
car.clear()

# Printing the dictionary after clearing all items
print(car)

#deleting the dictionary completely
del car




#Exercise5 Looping through a dictionary and cretaing a nested dictionary
car = {
    'name':'Spacio',
    'model':'2017 model',
    'milage':110
}
# Looping through the dictionary
for key, value in car.items():
    print(key, "->", value)
    
# Creating a nested dictionary
car = {
    'name': 'Spacio',
    'model': '2017 model',
    'specs': {
        'mileage': 110,
        'color': 'blue',
        'engine': '2.0L',
        'transmission': 'Automatic'
    },
    'owners': [
        {'name': 'John', 'age': 35},
        {'name': 'Lisa', 'age': 28}
    ]
}

# Accessing values in the nested dictionary
print(car['specs']['mileage']) 
print(car['owners'][0]['name'])  






#Number Datatypes
# Integer
integer_num = 10
print(integer_num, type(integer_num))  

# Float
float_num = 3.14
print(float_num, type(float_num))  

# Complex
complex_num = 2 + 3j
print(complex_num, type(complex_num))  



# Conversions
# Integer to String
num = 123
num_str = str(num)
print(num_str, type(num_str))  

# String to Integer
num_str = '456'
num = int(num_str)
print(num, type(num))  

# Float to Integer
float_num = 3.14
int_num = int(float_num)
print(int_num, type(int_num))  

# Integer to Float
int_num = 7
float_num = float(int_num)
print(float_num, type(float_num)) 

# Integer to complex
int_num = 7
complex_num = complex(int_num)
print(complex_num, type(complex_num)) 





#Strings
#Exercise one determining the length using len()
name = "Vanessa"
name_length = len(name)
print(name_length, name)

#Exercise two using a loop
word = "Hello"
for i in word:
    print(i)

#Exercise three Using slicing
#return a given range of characters
stmt = "My name is Vanessa "
print(stmt[2:7])
print(stmt[:5])

#Conacatenation(addition of strings)
greeting1 = "Hello"
greeting2 = "There"

print(greeting1 + greeting2 + "How are you doing")

#format strings
stmt = "My name is Nessa am {} years"
age = 15
print(stmt.format(age))


#Booleans
#Exercise for using boolean
if 9<6:
    print("True")
else:
    print("False")