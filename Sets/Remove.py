
# REMOVE SET ITEMS
   
           # To remove an items in a set, use the remove() or the discared() method.


# 1. Remove() -- Removes a specific item.

fruits = {"apple","banana","cherry"}
fruits.remove("apple") 
print(fruits)               # {'banana', 'cherry'}

       # If the item does not exist, it will raise an error.



# 2. Discard() -- Remove a specific item safety.

fruits = {"apple","banana","cherry"}
fruits.discard("banana")
fruits.discard("pineapple")
print(fruits)              # {'cherry', 'banana'}



# 3. pop() -- Removes a random item.
 
fruits = {"apple","banana","cherry","kiwi"}
removed_item = fruits.pop()
print("removed :",removed_item)         # removed : apple
print("Remaning set :", fruits)         # Remaning set : {'banana', 'cherry', 'kiwi'}


# 4. Clear() -- Removes all items
fruits = {"apple","banana","cherry"}
fruits.clear()
print(fruits)          # set() 



