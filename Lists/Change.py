
 # CHANGE LISTS 
      # To change the value of specific item, refers to the index number.

x = [1,2,3,4,5]
x[1] = 429
print(x)       # [1, 429, 3, 4, 5]


x = [1,2,3,4,5]
x[1:3] = [34,45]
print(x)        # [1, 34, 45, 4, 5]


x = [1,2,3,4,5]
x[1:4] = [12]
print(x)        # [1, 12, 5]


x = [1,2,3,4,5]
x[:3] = [23]
print(x)        # [23, 4, 5]