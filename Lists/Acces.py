
# ACCESS LIST ITEMS

      # same as slicing

# Lists are indexed starting from 0.

x = [1,2,3,4,5,6]
print(x[0])   # 1
print(x[1])   # 2
print(x[2])   # 3
print(x[3])   # 4
print(x[4])   # 5
print(x[5])   # 6


# Negative indexed
print(x[-1])   # 6

# Range of indexes:

x = [11,12,13,14,15,16]
print(x[3:])   # [14, 15, 16]           # this, start index 3 means 14
print(x[:3])   # 11, 12, 13]            # this, ends in index 3 means 14 but always stop in index .
print(x[-2:-1])  # [15]                 # this, reverse start -2 means 15 , -1 means 16 step goes and stops with 15.
print(x[::-1])   # [16, 15, 14, 13, 12, 11]       # this always reverse the lists

for y in x:
    print(y)       # 11
                   # 12
                   # 13
                   # 14
                   # 15
                   # 16


# Exists :
x = [1,2,3,4,5]
if 2 in x:
    print("yes")    # yes