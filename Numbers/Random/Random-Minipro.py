import random

# Take input from user
x = input("enter numbers : ")

# Convert each number to float (so both int and float inputs work)
numbers = [float(num) for num in x.split()]

# Pick one number randomly
choosen = random.choice(numbers)
print(f"the random number : {choosen}")
print(f"the integer is : {int(choosen)}")
print(f"the float is : {float(choosen)}")
print(f"the float is : {float(choosen):.4f}")
