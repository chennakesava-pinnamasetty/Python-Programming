
# ACCESS TUPLE
      # You can access tuple items by refering th the index number, inside square brackets.

# Tuples are ordered, so you can access their items using index numbers.

fruits = ("apple","banana","cherry")
print(fruits[0])      # apple
print(fruits[1])      # banana
print(fruits[-1])     # cherry


# ACCESS A RANGE (SLICING)

fruits = ("apple","banana","cherry","mango","orange")
print(fruits[1:4])     # ('banana', 'cherry', 'mango')
print(fruits[:3])      # ('apple', 'banana', 'cherry')
print(fruits[2:])      # ('cherry', 'mango', 'orange')
print(fruits[-4:-1])   # ('banana', 'cherry', 'mango')
print(fruits[::-1])    # ('orange', 'mango', 'cherry', 'banana', 'apple')


