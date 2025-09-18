
# In python , we hav e two types of formating strings

# 1. f- String
# 2. format() method


# 1. f-string
      # F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
     # To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
name = "chenna"
age = 21
print(f"My name is {name} and my age is {age} years old.")  # My name is chenna and my age is 21 years old.


# 2. formating() method
name = "chenna"
age = 21
print(" my name is {} and my age is {}".format(name,age))   # my name is chenna and my age is 21



# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)    # The price is 59.00 dollars


# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)        # The price is 1180 dollars