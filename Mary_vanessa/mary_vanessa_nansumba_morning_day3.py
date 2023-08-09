#Membership Operators:
#In:'in'operator :checks if a value exists in a sequence
#Not in:'not in'operator:checks ifa value  does exist in a sequence
#Identity Operators:
#Is:'is'operator:checks if two values are the same
#Is not:'is not'operator:checks if two values are not the same

#Examples of arithmetic operators
#Addition
# x = 100 + 45
#print(x)
#Subtraction
#y=50-15
#print(y)
#Multiplication
#z=50*5
#print(z)
#Division
#a=50/45
#print(a)
#modulus
#e=50%2
#print(e)
#Exponentiation
#d=2**2
#print(d)
#Examples of comparsion
#Comparison Operators
#a=100
#b= 55
#Greater than
#if a > b:
 #   print("a is greater than b")
  #  print(a>b)
#Less than
#if a < b:
   # print("a is less than b")
  #  print(a<b)
#Greater than or equal to
#if a >= b:
   # print("a is greater than or equal to b")
    #print(a>=b)
#Less than or equal to
#if a <= b:
   # print("a is less than or equal to b")
    #print(a<=b)
#Equal to
#if a == b:
   # print("a is equal to b")
   # print(a==b)
#Not equal to
#if a != b:
   # print("a is not equal to b")
   # print(a!=b)
#Less than or equal to
#print(a<=b)
#Equal to
#print(a==b)
# Example with Logical Operators
#Logical Operators
#a = True
#b = False

#Logical AND
#print( a and b)
#Logical OR
#print( a or b)
  #Logical NOT
#print(not a) 
#print (not b)


#Modulus and Assign
#e= 18
#e%=5
#print( e)

#Exponential and Assign
#f = 2
#f **= 4
#print( f)
#Membership assignment Operators
#Cars =['Jeep','Telsa','BMW','RollRoyce']
#if 'Jeep' in Cars:
 #   print( 'Jeep is in list')
  #  print('Telsa'in Cars)
   # print('ROLL' in Cars)
#Identity Operators
#x = 20
#y=20
#is operator
#print(x is y)
#print(x is not y)
#print(x == y)
#print(x != y)
#print(x < y)
#print(x <= y)
#List
#is not operator
#z=[1,2,3,4,5,6,7,8,9]
#w=[1,2,3,4,5,6,7,8,9]
#print(z is w)
#print(z is not w)
#Bitwise operators
"""
Bitwise operstors are used to perform operations on individual bits in of binary numbers.
Bitwise AND ("&")
Bitwise OR ("|")
Bitwise XOR ('^'): Perform a bitwise XOR operation
Bitwise NOT ("~"):Peform a bitwise NOT operation between the corresponding
Bitwise left shift()
"""
#Examples of Bitwise operations
#print("Results of Bitwise operators")
#a =12 # binary: 1100
#b = 7 # binary: 0111

#result_and = a & b # binary: 0100 (decimal: 4) print("Bitwise AND result:", result_and)

# Bitwise OR example

#result_or = a | b# binary: 1111 (decimal: 15) print("Bitwise OR result:", result_or)

# Bitwise XOR example

#result_xor = a ^ b # binary: 1011 (decimal: 11) print("Bitwise XOR result:", result_xor)

# Bitwise NOT example

#a= 42 # binary: 00101010

#result_not = ~a # binary: 11010101 (decimal: -43)

#print("Bitwise NOT result:", result_not)

#Bitwise Left shift example

#a= 5 # binary: 00000101

#shifted_left = a << 2 # binary: 00010100 (decimal: 20)

#print("Bitwise left shift result:", shifted_left)

#Bitwise right shift example

#a = 16 # binary: 00010000

#shifted_right = a >> 3 # binary: 00000010 (decimal: 2) print("Bitwise right shift result:", shifted_right)

#Example and execrise
#tkinter learn 
#Assignment create a simple calculator program with a GUI interface.
#Make the title of the  calculator program window with your name e.g "Jeff Geoff simple Calculator"
#Assigment
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Nansumba mary vanessa simple calculator")

# Create an entry field
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators
button_1 = tk.Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=10, command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=20, pady=10, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=20, pady=10, command=lambda: button_click("/"))
button_equal = tk.Button(root, text="=", padx=20, pady=10, command=button_equal)

# Position the buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)

# Start the main event loop
root.mainloop()
