
# Type Conversion :
    # Changing a value from one data type to another - eitherautomatically ( implict ) or manually ( explicit )


# Implicit Conversion
      # Done by python automatically.

x = 5
y = 10.7
z = x + y
print(z)            # 15.7
print(type(z))      # <class 'float'>



# Explicit Conversion
     # Done by you -- also called "casting"

x = 10
y = float(x)
print(y)            # 10.0
print(type(y))      # <class 'float'>



         # ==== HINT ====

# Type casting is a part of type conversion
# All type casting is type conversion but not all type conversion is casting ( because some are automatic)