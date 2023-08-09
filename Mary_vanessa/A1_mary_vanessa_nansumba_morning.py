# Regular expressions
"""
_`.` (dot): Matches any single character.
- `*`: Matches zero or more occurrences of the previous character or group.
- `+`: Matches one or more occurrences of the previous character or group.
- `?`: Matches zero or one occurrence of the previous character or group.
- `[]`: Matches any character within the brackets.
- `()` (parentheses): Groups multiple characters or expressions together.
- `|` (pipe): Matches either the expression before or after it.
- `^` (caret): Matches the start of a string.
- `$` (dollar sign): Matches the end of a string.
- `\d`: Matches any digit (0-9).
- `\w`: Matches any word character (alphanumeric and underscore).
- `\s`: Matches any whitespace character (space, tab, newline).
- `\b`: Matches a word boundary.
"""

#examples
# import re

# string = "Good, Morning!"
# #pattern = r"GOOD"
# pattern = r"Good"

# match = re.search(pattern, string)
# if match:
#     print("Pattern found")
# else:
#     print("Pattern not found")



# string = "Nansumbamary@gmail.com"
# pattern = r"(\w+@\w+\.\w+)"

# match = re.search(pattern, string)
# if match:
#     email = match.group(1)
#     print("Email:", email)
# else:
#     print("Email not found")

# practice
# import re

# def validate_password(password):
    # Minimum 8 characters, maximum 20 characters
    # At least one uppercase letter
    # At least one lowercase letter
    # At least one digit
    # At least one special character from !@#$%^&*()_+=-{}[],.<>
    
#     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+=-{}[\],.<>])(?=.*[a-zA-Z\d!@#$%^&*()_+=-{}[\],.<>])[A-Za-z\d!@#$%^&*()_+=-{}[\],.<>]{8,20}$"
    
#     if re.match(pattern, password):
#         return True
#     else:
#         return False
    
# password = input("Enter your password: ")
# if validate_password(password):
#     print("Password is valid.")
# else:
#     print("Password is not valid.")


# Generators and Iterators
# 'yield'generator 
# Iterator '__iter__' "__next__" Iterator 

# def factorial(x):   
#     if x == 0: 
#          return 1
#     else:
#         return x * factorial(x - 1)

# print the factorial of a number 1-10
# for i in range(1,11):
#     print(i, factorial(i))

#Example 

#Generate function that yields the square of numbers from 1-10

# def squares():
#     for i in range(1,10):
#         yield i ** 2

#create an iterator object that yields the square of numbers from 1-10
# squares_iterator = squares()

#Print the first 5 square of numbers from 1-10
# for i in range(8):
#     print(next(squares_iterator))

# Decorators @my_decorator

# def my_decorator(func):
#     def inner():
#         print("This is my decorator")
#         func()
#     return inner
# @my_decorator
# def outer_decorator():
#     print("This is my outer decorator")

# outer_decorator()

#practice

# Generator function for even numbers
# def even_generator(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i

# Create an iterator using the generator function
# even_numbers_iterator = even_generator(20)

# Iterate over the values using the iterator
# for num in even_numbers_iterator:
#     print(num)

# multi processing
#Example of multi processing

# import multiprocessing

# def square(number):
#     result = number ** 2
#     print("multi processing result: ")
#     print(f"Square of {number}: {result}")

# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Create a process pool with maximum number of CPU cores
    # pool = multiprocessing.Pool()

    # Apply the `square` function to each element in `numbers` in parallel
    # pool.map(square, numbers)

    # Close the pool and wait for all processes to finish
    # pool.close()
    # pool.join()

# multi threading
#example
# import threading

# def square(number):
#     result = number ** 2
    # print("multithreading output")
#     print(f"Square of {number}: {result}")

# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#     # Create a thread for each number in the list
#     threads = []
#     for number in numbers:
#         thread = threading.Thread(target=square, args=(number,))
#         threads.append(thread)
#         thread.start()

    # Wait for all threads to finish
    # for thread in threads:
    #     thread.join()