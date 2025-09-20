
# ADD LISTS

# APPEND : Add item to the end automatically.
# INSERT : Based index, we can insert spcified place.
# EXTEND : Combining two list.

# APPEND
x = [1,2,3,4]
x.append(456)
print(x)   # [1, 2, 3, 4, 456]


# INSERT
x = [1,2,3,4,5]
x.insert(3,121)
print(x)    # [1, 2, 3, 121, 4, 5]


# EXTEND
x = [1,2,3]
y = [4,5,6]
x.extend(y)
print(x)     # [1, 2, 3, 4, 5, 6]