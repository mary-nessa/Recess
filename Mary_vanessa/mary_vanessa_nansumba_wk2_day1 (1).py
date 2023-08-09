# class Car:
#     def _init_(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def start_engine(self):
#         print("Engine started"

#     def stop_engine(self):
#         print("Engine stopped")


# car1 = Car("tesla", "model s", 2022)
# print(car1.make)
# print(car1.model)
# car1.start_engine()
# car1.stop_engine()


# class BankAccount:
#     def _init_(self, account_number, account_holder, balance=0.0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit of $%.2f successful. New balance: $%.2f" %
#               (amount, self.balance))

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print("Withdrawal of $%.2f successful. New balance: $%.2f" %
#                   (amount, self.balance))
#         else:
#             print("Insufficient funds. Withdrawal canceled.")

#     def display_balance(self):
#         print("Account holder: %s" % self.account_holder)
#         print("Account number: %s" % self.account_number)
#         print("Current balance: $%.2f" % self.balance)


# # Creating a bank account
# account = BankAccount("123456789", "John Alexander", 1000.0)

# # Displaying account information
# account.display_balance()

# # Making a deposit
# account.deposit(500.0)

# # Withdrawing money
# account.withdraw(200.0)

# # Trying to withdraw more than the available balance
# account.withdraw(1500.0)

# # Displaying final account balance
# account.display_balance()


# # Rectangle
# class Rectangle:
#     def _init_(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)


# # Creating a rectangle object
# rectangle = Rectangle(5, 7)

# # Calculating and printing the area
# area = rectangle.calculate_area()
# print("Area:", area)

# # Calculating and printing the perimeter
# perimeter = rectangle.calculate_perimeter()
# print("Perimeter:", perimeter)


# # University Student
# class Student:
#     def __init__(self, name, year,course):
#             self.name = name
#             self.year = year
#             self.course = course
    
#     def display_detials(self):
#       print("Name:",self.name)
#       print("Year:",self.year)
#       print("Course:",self.course)

# # Create a student object
# my_student = Student("maryvanessa",3, "Software Engineering")
# # Display the student details
# my_student.display_detials()
# # Object
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#             print("Hello, my name is", self.name)
#             print("I am", self.age, "years old.")
# # Create a Person object
# my_person1 = Person("mary",20)
# my_person2 = Person("vanessa",19)

# #Acess the Person object attributes
# print(my_person1.name)
# print(my_person1.age)
# print(my_person2.name)
# print(my_person2.age)

# # Invoke our object method
# my_person1.greet()
# my_person2.greet()


# #  ExERCISE 1
# # Calculate the area and circumference of a circle


# #Circle
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14 * self.radius * self.radius

#     def calculate_circumference(self):
#         return 2 * 3.14 * self.radius
# # create a circle object
# my_circle = Circle(7)
# # display the circle
# print(my_circle.radius)
# print(my_circle.calculate_area())
# print(my_circle.calculate_circumference())


# Exercise 2

# calculate  and display employee  bonuses(15%) of salary(employee1:150000, employee2: 230000)
# bonus (15%) of salary(employee
#class Employee:
    #def __init__(self, name, salary):
       # self.name = name
       # self.salary = salary

    # def calculate_bonus(self):
      #  return self.salary * 0.15

    # def display_bonus(self):
        #print("employe", self.calculate_bonus())

# create  object 
# my_employee1 = Employee("mary", 150000)
# my_employee1.display_bonus()
# my_employee2 = Employee("vanessa", 230000)
 # my_employee2.display_bonus()

# Encapsulation
# key  main goals of encapsulation are
"""
1. To protect the object from changes
2. To protect the object from external changes
3. Code organization and modularity
4. To hide the implementation details of an object
"""
# Example 4: with a bank account
# class BankAccount:
#     def __init__(self, account_number,balance):
#         # encapsulation of the account number info
#         self._account_number = account_number #
#         self._balance = balance

#     def deposit(self,amount):
#         self._balance += amount

#     def withdraw(self,amount):
#         if self._balance >= amount:
#             self._balance -= amount
#         else:
#             print("not enough funds...")

#     def get_balance(self):
#         return self._balance
#     #Create a bank  object
# my_account =BankAccount("1234567",70000)
# # display the account
# print(my_account._account_number)
# print(my_account._balance)
# my_account.deposit(10000)
# print(my_account._balance)
# my_account.withdraw(10000)
# print(my_account._balance)
                             
# Exercise 2 : Covert temperature (37 celsius) to fahrenheit
# class Temperature:
#     def convert(self, temp):
#         self._temp = temp

#     def fahrenheit(self):
#         return (self._temp * 9/5) + 32  

#object
# my_temp = Temperature()
# my_temp.convert(37)
# print(my_temp.fahrenheit())

# Assigment1: show encapsulation with employee information to give a 
# pay increment( Salary with employee information to new salary) e.g from 850000 t0 1000000
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

        self._pay_increment = (self._salary * 0.18)
        self._new_salary = self._salary + self._pay_increment
        self._new_salary = self._new_salary
    def display_employee_info(self):
        print("Name:",self._name)
        print("Salary:",self._salary)
        print("Pay Increment:",self._pay_increment)
        print("New Salary:",self._new_salary)
        
my_employee1 = Employee("vanessa",850000)
my_employee1.display_employee_info()
my_employee2 = Employee("mary",700000)
my_employee2.display_employee_info()
