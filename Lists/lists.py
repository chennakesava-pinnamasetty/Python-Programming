
# LISTS
     # Lists are used to store  multiple items in a single variable.

# Lists are one of 4 built-in data types in python used to store collections of data.
# The other 3 are Tuple,Set and Dictinory all with different quality and usage.


# LIST ITEMS : Orderd, changeable nad allow duplicates values lists are  indexed.

# ORDERED :
   # Lists are odered it means that the items have defined order, and that will not change.

# ex:
x = [1,2,3,4,5]
print(x)     # [1, 2, 3, 4, 5]
                         # When you access or loop through the list, elements will always appear in that same sequence — unless you change it.


# CHANGABLE :
     # Lists are Orderd, it means that the items have defined order, and that will not change.

x = [1,2,3,4,5]
print(x[0])    # 1
print(x[1])    # 2
print(x[2])    # 3
print(x[3])    # 4
print(x[4])    # 5

 # if you want add extra one but it placed automatically in the last.
x = [1,2,3,4,5]
x.append(8)
print(x)       # [1, 2, 3, 4, 5, 8]


x = [1,2,3,4,5]
for y in x:
    print(y)     # 1
                 # 2
                 # 3
                 # 4
                 # 5

# CHANGABLE:
     # Meaning that , we can change,add and remove
x = [1,2,3,4,5]
x.pop(3)          # [1, 2, 3, 5]
x.append(10)       # [1, 2, 3, 4, 5, 10]
x.insert(1,11)     # [1, 11, 2, 3, 4, 5]
print(x)



# ALLOW DUPLICATES
    # Lists are indexed, lists can have items with the same velue.

x = [1,2,3,1,2,3]
print(x)          # [1, 2, 3, 1, 2, 3]


x = [1,2,'rt',10.3,8,9]
print(len(x))   # 6
print(type(x))  # <class 'list'>

# We also use double round brackets:
x = list((1,2,4,5))
print(x)   # [1, 2, 4, 5]