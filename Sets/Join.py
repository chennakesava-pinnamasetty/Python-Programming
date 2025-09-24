
# JOIN SETS


# 1. union() -- Returns a new set.

       # Join set1 and set2 into anew set.
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)        # {'a', 1, 2, 'b', 3, 'c'}


# multiple sets -- Join multiple sets with union() method.

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"chenna","kesava"}
set4 = {"apple","banana","cherry"}
my_set = set1.union(set2,set3,set4)
print(my_set)          # {1, 2, 3, 'kesava', 'b', 'banana', 'c', 'chenna', 'apple', 'cherry', 'a'}



# 2. USING | (pipe operator)
set1 = {1,2,3}
set2 = {3,4,5}
result = set1 | set2
print(result)      # {1, 2, 3, 4, 5}

# multiple

set1 = {1,2,3}
set2 = {3,4,5}
set3 = {"chenna","kesava"}
set4 = {"apple","banana","cherry"}
my_set = set1|set2|set3|set4
print(my_set)        # {1, 2, 3, 4, 5, 'banana', 'kesava', 'cherry', 'chenna', 'apple'}



# 3. Using update() ( adds items too an existing set).
        # The update() method inserts all items from one set into another.
        # The update() changes the original set, and does not return a new list.

set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)         # {'a', 1, 'c', 2, 3, 'b'}


# NOTE : Both union() and update() will exclude any duplicate items.
