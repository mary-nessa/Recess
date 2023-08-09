
# Execption handling
"""
1. Purpose of Exception Handling: Exception handling helps prevent your program from abruptly terminating when errors occur. 
It allows you to catch, handle, and recover from exceptions, ensuring that your program continues running and providing meaningful error messages to users.
"""

# try:
#     a= int(input("Enter number: "))
#     b= int(input("Enter number: "))
#     result = a/ b
#     print("The result is:", result)
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("We cant divide by zero. Please enter a valid")
# except Exception as e:
#     print("An error occurred:", str(e))
# finally:
#     print("thank you!")
# # IndexError
# my_numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
# try:
#     index = int(input("Enter an index: "))
#     value = my_numbers[index]
#     print("The value at index", index, "is:", value)
# except IndexError:
#     print("Error: Index is out of bound.")

# file handling
# steps to follow when working with files
"""
1.Open the File: Use the `open()` function to
open the file. Specify the file path and
the mode in which you want to open the file (e.g., read mode, write mode, append mode).
2.Perform Required Operations after the file is opened:
   - Read from File: If you want to read the contents of the file, 
   use methods like `read()`, `readline()`, or `readlines()` to access the data.
   - Write to File: If you want to write or overwrite data in the file, 
   use the `write()` method to add content.
    - Append to File: To append data to an existing file,
     open the file in append mode and use the `write()` method to add content.
3. Close the File: After you have finished working with the file, 
it is important to close it using the `close()` method. This ensures that any changes are saved and resources are released.
 """
# Opening a file in write mode
import os


file = open("nessa.txt", "w")

# Writing content to the file
file_path = "nessa.txt"

if os.path.exists(file_path):
    print("File exists.")
else:
     print("File does not exist.")

file.write("Hello, nessa!\n")
file.write("This is what you have written.\n")
file.write("this  is new content")
# Closing the file
file.close()

 # Opening the file in read mode
file = open("nessa.txt", "r")

 # Reading the content of the file
content = file.read()
print(" Contents:\n", content)

 # Closing the file
# file.close()
# Opening  the file in append mode
file = open("nessa.txt", "a")

# Append content to the file
file.write("This is more content to the file.\n")
file.write("additional data.")

# Close the file
file.close()

# Opening the file in read mode
file = open("nessa.txt", "r")
content = file.read()
print(" Contents:\n", content)
file.close()
