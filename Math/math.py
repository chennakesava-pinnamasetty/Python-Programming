

# Python has built-in operators and a math module that gives extra mathematical functions.


# 1 .ARITHMETIC OPERATORS

'''
a = 10
b = 5

print("add : ",a+b)
print("sub :",a-b)
print("mul :",a%b)
print("div :",a/b)
print("floor div :",a // b)
print("modulos :",a & b)
print("Exponentiation :",a ** b)

# output :

add :  15
sub : 5
mul : 0
div : 2.0
floor div : 2
modulos : 0
Exponentiation : 100000
'''



# 2. Built-in functions
'''
print(abs(-5))      # 5 → Absolute value
print(round(3.567)) # 4 → Rounded
print(pow(2, 3))    # 8 → Power (same as 2**3)

'''

# 3 math

#import math
'''
print(math.sqrt(16))      # 4.0 → Square root
print(math.factorial(5))  # 120
print(math.ceil(4.2))     # 5 → Ceiling (next integer)
print(math.floor(4.9))    # 4 → Floor (previous integer)
print(math.fabs(-7))      # 7.0 → Absolute (float)
'''

# 4. Constants
'''
print(math.pi)   # 3.14159...
print(math.e)    # 2.71828...
print(math.inf)  # Infinity
print(-math.inf) # -Infinity
'''

# 5. Trigonometry

'''
# (Angles are in radians by default.)

print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0
print(math.tan(math.pi/4))  # 1.0

# Convert degrees ↔ radians
print(math.radians(180))  # 3.14159 (π)
print(math.degrees(math.pi)) # 180.0
'''

# 6. Logarithms
'''
print(math.log(100))       # ln(100) → natural log
print(math.log10(100))     # log base 10 → 2
print(math.log2(8))        # log base 2 → 3
'''


# 7. GCD & LCM
'''
print(math.gcd(12, 18))   # 6
print(math.lcm(12, 18))   # 36
'''

# 8. Random Numbers (with random module)

'''
import random

print(random.random())       # Random float 0–1
print(random.randint(1, 10)) # Random int between 1 and 10
print(random.choice([2,4,6,8])) # Random element from list

'''



# 9. Min , Max

'''
x = max(1, 4, 7)     # 7
y = min(2, 4, 9)     # 2

print(x)
print(y)
'''



