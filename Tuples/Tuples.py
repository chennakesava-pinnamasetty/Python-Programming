
# What is tuples ?
    # A tuple is immutable -->  once you create it,you can't change it(no adding, removing or updating elements).
    # It can store multiple values in one variable.
    # Values can be of different data types.


# 1. Creating Tuple
my_tuple = (10,20,30)
mixed_tuple = ("aple",5,True,3.14)
single_tuple = (5,)

print(my_tuple)        # Tuples with multiple items
print(mixed_tuple)     # Tuple with diff data typles
print(single_tuple)    # Tuples with one item ( must have comma )


# 2. Accessing tuple elements.
fruits = ("apple","banana","cherry")
print(fruits[0])        # apple
print(fruits[1])        # banana
print(fruits[-1])       # cherry


# 3. Why tuples are usseful
    # Data safety -->  Since they can't be changed, they are safe for storing constant values.
    # Faster than lists for iteration.
    # Can be used as dictionary keys (list cannot).


# Tuple Methods
     # Tuples have only two methods.

numbers = (1,2,3,4,2,7,2)
print(numbers.count(2))   # 3      How many times 2 appears      ->  3
print(numbers.index(3))   # 2      Position of first ocurance of 3   -> 2


# Tuple Unpacking
     # You can directly assign tuple values to variables.

person = ("chenna",22,"kesava")
fname,age,lname = person

print(fname)      # chenna
print(age)        # 22
print(lname)      # kesava



# Quick Example:
coordinates = (5,10)
x,y = coordinates
print(f"x = {x}, y = {y}")      # x = 5, y = 10





# Tuple Items
      # Tuple items are ORDERED, UNCHANGEABLE, and ALLOW DUPLICATES.
      # Tuple items are indexed, the first item has indexed [0], the second item has indexed [1] etc..,

# ORDERED :
     # When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

numbers = (1,2,3,4,5)
print(numbers[0])      # 1
print(numbers[-1])     # 5


# UNCHANGEABLE :
     # Tuples are unchangeable, meaning that we can'y change, add or remove items after the tuple has been created.

#fruits = ("apple","banana","cherry")
#fruits[0] = "mango"
#print(fruits)            # TypeError: 'tuple' object does not support item assignment.


# Allow Duplicates.
      # Since tuples are indexed, they can have items with the same value.

fruits = ("apple","banana","kiwi","apple")
print(fruits)         # ('apple', 'banana', 'kiwi', 'apple')



# LENGTH
fruits = (1,2,3,4,5)
print(len(fruits))   # 5

# TYPE
fruit = ("apple")
print(type(fruit))     # <class 'str'>

fruit = ("apple",)
print(type(fruit))     # <class 'tuple'>


# For
fruits = ("apple")
for x in fruits:
    print(x)