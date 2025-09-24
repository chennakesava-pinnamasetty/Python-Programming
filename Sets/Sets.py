
# SETS

     # A set is a collection of unodered, unchangeable ( immutable elements, but you can add/ remove items ).
     # Sets are written { } braces.
     # Duplicates are automatically removed.

# If you run several time, the values order changes several times.

fruits = {"apple","banana","cherry","kiwi"}
print(fruits)      # {'kiwi', 'apple', 'banana', 'cherry'}
                   # {'banana', 'apple', 'kiwi', 'cherry'}

    # Order is not guaranteed.
    # Duplicates are removed.



# KEY POINTS
     
      # 1. Unordered : Items don't have an index.
      # 2. No duplicate : Repeated items are ignored.
      # 3. Mutable container : you can add / remove items
      # 4. Immutable elements : Elements themseleves must be immutable.



# EX : True and 1 is considered the same value.
fruits = {"apple","banana",True,2.9,"kiwi",9}
print(fruits)       # {True, 2.9, 'banana', 9, 'kiwi', 'apple'}


# EX : False and 0 is considered the same value.
fruits = {"apple","banana",False,2.9,"kiwi",9}
print(fruits)    # False, 'kiwi', 2.9, 'apple', 'banana', 9}


# lens()
fruits = {"apple","banana","cherry"}
print(len(fruits))     # 3


# Sets items - Data types
set1 = {"apple","banana","cherry","kiwi"}
set2 = {1,3,4,6,7,2}
set3 = {True,False,True,False}

print(set1)         # {'kiwi', 'banana', 'apple', 'cherry'}
print(set2)         # {1, 2, 3, 4, 6, 7}          
print(set3)         # {False, True}



# Type()
     
     # set constructor :
fruits = set(("apple","banana","cherry"))
print(fruits)       # {'apple', 'cherry', 'banana'}