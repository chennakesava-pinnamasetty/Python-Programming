
# ACCESS SETS

     # sets are unordered, so you cannot access by index, like you do with lists or tuples.


# 1. LOOP THROUGH THE SET

fruits = {"apple","banana","cherry"}
for i in fruits:
    print(i)       # apple
                   # banana
                   # cherry
                                  # Output order may change each time you run it.


# 2. CHECK IF AN ITEMS EXISTS (membership list)

fruits = {"apple","banana","cherry","kiwi"}
if "banana" in fruits:
    print("yes, banana is in the list.")
                 # yes, banana is in the list.


# 3. CONVERT SET TO LIST / TUPLE TO USE INDEXING.

my_set = {"apple","banana","cherry"}
my_list = list(my_set)
print(my_list[0])         # apple

