
# REMOVE LISTS

# REMOVE() : This removes the specified item.
# POP()    : Based on index removed specified item.
# DEL      : del keyword also remove the specified index.
# CLEAR()  : This empties the list, still remains but no content.


# REMOVE()
x = [1,2,3,4,5]
x.remove(3)
print(x)           # [1, 2, 4, 5]

# POP()
x = [1,2,3,4,5]
x.pop(3)
print(x)         # [1, 2, 3, 5]

# DEL
x = [1,2,3,4,5]
del x
print(x)            # NameError: name 'x' is not defined


# CLEAR()
x = [1,2,3,4,5]
x.clear()
print(x)      # []