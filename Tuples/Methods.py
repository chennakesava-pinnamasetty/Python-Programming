
# TUPLE METHODS

   # In python, tuples has two build-in methods
       # 1. count
       # 2. indexed


# COUNT
    
     # Returns the number of times as specified value occurs in a tuple.

tuple = (2,3,2,4,2,3,5,2,7,4)
x = tuple.count(2)
print(x)     # 4



# INDEXED 
     
     # Searches the tuple for a specified value and returns the position of where it was found.

x = (1,3,7,2,6,7,9,0)
y = x.index(7)
print(y)   # 2