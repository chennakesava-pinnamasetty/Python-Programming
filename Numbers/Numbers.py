# In python have three numeric types:
      # integer
      # float
      # complex

# numbers are a build in datatypes used to perform mathematical operators.
# python supports several types of numbers, each with specific usecases.

x = 10
y = 10.9
z = 10j
print(type(x))        # <class 'int'>
print(type(y))        # <class 'float'>
print(type(z),"\n")   # <class 'complex'>


# 1. Integers 
      # Whole numbers, positive or negative without decimal points.
      # No size limit in python ( you can store very large integers ).

a = 10
b = -99
c = 1000000

print(type(a))       # <class 'int'>
print(type(b))       # <class 'int'>
print(type(c),"\n")  # <class 'int'>


# 2. Floating point
      # Numbers with a decimal point
      # also suppoets scientific notation ( e.g., 1.5e3 means 1.5 x 10³)

x = 3.14
y = 0.001
z = 2.5e3

print(type(x))        # <class 'float'>
print(type(y))        # <class 'float'>
print(type(z),"\n")   # <class 'float'>


# 3.Complex numbers 
     # Used in mathematical to prepresent numbers with a real + imaginary part.
     # Written as a+b, where j is the imaginary part.

c1 = 2 + 3j
c2 = 5j
print(type(c1))    # <class 'complex'>
print(type(c2))    # <class 'complex'>

# You can also acess
print(c1.real)     # 2.0
print(c1.imag)     # 3.0 

print(c2.real)     # 0.0
print(c2.imag)     # 5.0