
# UPDATE TUPLES
      # Tuples are unchangeable, meaning that you cannot change, add (or) remove, items once the tuple is created.


# CHANGE TUPLE
     # Convert the tuple into list to be able to change it.

x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)          # ('apple', 'kiwi', 'cherry')


# ADD ITEMS
 
fruits = ("apple","banana","cherry")
y = list(fruits)
y.append("orange")
fruits = tuple(y)
print(fruits)       # ('apple', 'banana', 'cherry', 'orange')

# OR

fruits = ("apple","banana","cherry")
y = ("orange",)
fruits += y
print(fruits)       # ('apple', 'banana', 'cherry', 'orange')



# REMOVE ITEMS
fruits = ("apple","banana","cherry")
y = list(fruits)
y.remove("apple")
fruits = tuple(y)
print(fruits)        # ('banana', 'cherry')



# DEL
fruits = ("apple","banana","cherry")
del fruits
print(fruits)       # NameError: name 'fruits' is not defined
