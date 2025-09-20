
# LIST COMPREHENSION
      # List comprehensive is a short and easy way to create a new list by looping through an existing list (for sequence) and possibily adding a condition.


# new_list = [expression for item in iterable if condition]

      # expression = what you want to strore in the new list.
      # item = variable that takes each value from the iterable.
      # iterable = sequence you are looping over (like a list, range,etc.,)
      # condition(optional) = filters items before adding to the new list.

# 1. Basic list comprehension.
numbers = [1,2,3,4,5]
square = [n**2 for n in numbers]
print(square)         # [1, 4, 9, 16, 25]


#2. With condition
number = [1,2,3,4,5]
even = [n for n in number if n%2 == 0]
print(even)      # [2, 4]

# 3. String 
fruits = ["apple","banana","cherry","kiwi","mango"]
new_list = [x for x in fruits if "a" in x]
print(new_list)       # ['apple', 'banana', 'mango']


# Range()
multi_3 = [n for n in range(1,21) if n % 3==0]
print(multi_3)        # [3, 6, 9, 12, 15, 18]


# Condition
fruits = ["apple","banana","kiwi","cherry","mango"]
new_list = [x for x in fruits if x != "apple"]
print(new_list)      # ['banana', 'kiwi', 'cherry', 'mango']


# Iterable
new_list = [x for x in range(10)]
print(new_list)       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = [x for x in range(10) if x<5]
print(new_list)         # [0, 1, 2, 3, 4]


# Expression
fruits = ["apple","mango","cherry","kiwi"]
new_list = [x.upper() for x in fruits]
print(new_list)      # ['APPLE', 'MANGO', 'CHERRY', 'KIWI']

the_list = ['hello' for x in fruits]
print(the_list)       # ['hello', 'hello', 'hello', 'hello']

