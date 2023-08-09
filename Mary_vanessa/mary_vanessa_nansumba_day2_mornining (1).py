#Control Flow

#if, elif, else statements
age = 9
#Example1
if age<18:
    print("You are under age")
elif age>= 18 and age <= 65:
    print("Your are an adult")
else:
    print("Your are a senior adult")
    
    
#loops(while, for)
#while loop
count = 0

while count < 5:
    print("Count:", count)
    count += 1

fruits = ["apple", "banana", "cherry"]

#for loop
for fruit in fruits:
    print("Fruit:", fruit)


#Continue and break statements
# continue statement is used to skip code during execution 
# break brings execution of code to an end when a condition is met

x = 0

while x < 50:
    x += 1  # Increment x by 1

    if x % 2 == 0:
        continue  # Skip even numbers

    if x > 10:
        break  # Exit the loop if x is greater than 10

    print(x)  # Print x if it is an odd number and less than or equal to 10

#Handling Exceptions
try:
    # Division by zero
    result = 10 / 0
    print("This will not be executed")
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("No exception occurred")
finally:
    print("Cleanup operations")

#Exercie
mental_health_states = {
    (1, 3): "You are experiencing significant challenges. Seek immediate assistance.",
    (4, 7): "Your mental health is fair. Consider seeking support.",
    (8, 10): "Your mental health is good. Maintain your well-being."
}

mental_health_scale = int(input("On a scale of 1 to 10, how is your mental health? "))

state_found = False

for state_range, description in mental_health_states.items():
    if state_range[0] <= mental_health_scale <= state_range[1]:
        print(description)
        state_found = True
        break

if not state_found:
    print("Invalid mental health scale. Please enter a number between 1 and 10.")


