
# ARITHMETIC OPERATORS 
   # Arithmetic operators are used with numeric values to perform common mathematical operations:
# Addition
# Subtraction
# Multiplication
# Division
# Modulus
# Exponentiation
# Floor division


# Addition
x = 5
y = 6
print(x+y)   # 11

# Subtraction
x = 6
y = 7
print(x-y) # -1

# Multiplication
x = 7
y = 5
print(x * y)   # 35

# Division
x = 9
y = 6
print(x / y)  # 1.5

# Modulus
x = 7
y = 3
print(x % y)  # 1

# Exponentiation
x = 4
y = 8
print(x ** y)   #65535

# Floor Division
x = 9
y = 6
print(x // y)  # 1



# write a program to take two integers from the user and print:


input("Enter the 1st number : ") # 15
y = int (input("enter the 2nd number : "))    # 2

print("sum : ", x + y)  # add  17
print("Diff :",x - y)   # sub  13
print(" Product :",x * y)  # mutli  30
print("Quotinent :",x / y)  # div   7.5
print("quotient (integer):",x // y)  # floor  7
print("Reminder :",x % y)   # mod    # 1



# 1. Write a program that asks the user for a number and prints its square and cube.

# Ask user for a number
num = float(input("Enter a number: "))

# Calculate square and cube
square = num ** 2
cube = num ** 3

# Print results
print("Square of", num, "is:", square)
print("Cube of", num, "is:", cube)

'''Enter a number: 4
Square of 4.0 is: 16.0
Cube of 4.0 is: 64.0
'''



# 2. Write a Python program to calculate the area of a circle given its radius.

# Program to calculate the area of a circle

# Import the math module for pi
import math

# Ask the user for radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area (πr²)
area = math.pi * radius ** 2

# Display the result
print("The area of the circle with radius", radius, "is:", area)

'''Enter the radius of the circle: 5
The area of the circle with radius 5.0 is: 78.53981633974483
'''



# 3. Write a Python program to convert temperature from Celsius to Fahrenheit.

# Program to convert Celsius to Fahrenheit

# Get temperature in Celsius from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display result
print(f"{celsius}°C is equal to {fahrenheit}°F")


'''Enter temperature in Celsius: 37
37.0°C is equal to 98.6°F
'''



# 4. Write a Python program to compute (a + b)² for given a and b.

# Program to compute (a + b)²

# Get input from user
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

# Calculate (a + b)² using formula: (a + b)² = a² + 2ab + b²
result = (a + b) ** 2

# Display the result
print(f"The value of (a + b)² for a = {a} and b = {b} is: {result}")

'''Enter value of a: 3
Enter value of b: 4
The value of (a + b)² for a = 3.0 and b = 4.0 is: 49.0
'''




