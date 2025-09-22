
# UNPACK TUPLES


# 1.PACKING : 
       # Packing means putting multiple values into single tuple.
   # When we create a tuple, We normally assign values to it, this is called packing a tuple.

fruits = ("apple","banana","cherry")
print(fruits)        # ('apple', 'banana', 'cherry')


# UNPACKING :
        # Unpacking means taking out the values from the tuple and assigning them to variables.

fruits = ("apple","banana","cherry")
(a,b,c) = fruits
print(a)      # apple
print(b)      # banana
print(c)      # cherry


# Unpacking with * (star operator)
fruits = ("apple","banana","cherry","mango","grape")
(a,b,*c) = fruits
print(a)      # apple
print(b)      # banana
print(*c)     # cherry mango grape

   # If you don't know excatly how many values are in the tuple.
   # You can use * to grab multiple items into a list.