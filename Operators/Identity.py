
# IDENTITY OPERATORS :
    # Identity operators are used to compare the memory location ( i.e., the identity ) of two objects, not their values.


# is     = Returns True both variables are same objects.
# is not = Returns True if both variables are not the same object.


# is :
  
x = ['apple','banana','cherry']
y = ['apple','banana','cherry']
z = x
print(x is y)   # False
print(x is z)   # True
print(y is z)   # False
print( x == y)  # True



# is not :

x = ['apple','banana','cherry']
y = ['apple','banana','cherry']
z = x
print(x is not y)   # True
print(x is not z)   # False
print(y is not z)   # True
print( x != y)      # False