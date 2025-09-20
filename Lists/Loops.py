
# LOOPS LIST
 
  # Why we use loops in lists?
    # To access each element one by one.

    # To process data without writing repeated code.

    # To search, update, or display elements.



# Using a for loop:

x = [1,2,3,4,5]
for y in x:
    print(y)    # 1
                # 2
                # 3
                # 4
                # 5


x = "banana"
for y in x:
    print(y)      # b
                  # a
                  # n
                  # a
                  # n
                  # a


# Using for loop with range()
x = [1,2,3,4,5]
for y in range(len(x)):
    print(y)           # 0
                       # 1
                       # 2
                       # 3
                       # 4



x = [1,2,3,4,5]
for y in range(len(x)):
    print(f"{y} ->",x[y])      # 0 -> 1
                               # 1 -> 2
                               # 2 -> 3
                               # 3 -> 4
                               # 4 -> 5


# Using a While Loop
i = 1
while i < 6:
    print(i)
    i += 1         # 1
                   # 2
                   # 3
                   # 4
                   # 5


x = [1,2,3,4,5]
i = 1
while i < 6:
    print(x)
    i += 1          # [1, 2, 3, 4, 5]
                    # [1, 2, 3, 4, 5]
                    # [1, 2, 3, 4, 5]
                    # [1, 2, 3, 4, 5]
                    # [1, 2, 3, 4, 5]
                    

# u can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.

x = [1,2,3,4,5]
i = 0
for i in range(len(x)):
    print(f"{i} ->",x[i])
    i += 1                 # 0 -> 1
                           # 1 -> 2
                           # 2 -> 3
                           # 3 -> 4
                           # 4 -> 5