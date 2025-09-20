
# COPY LISTS

# 1. SHALLOW COPY 
       # Create a new list but references same inner object.
         # Shallow copies duplicates only the outer list structure,not the nested pbjects inside.

list1 = ["apple","banana","cherry"]
list2 = list1.copy()
list3 = list(list1)
list4 = list[:]
list1[0] = "mango"
print("list1 :",list1)        # list1 : ['mango', 'banana', 'cherry']
print("list2 :",list2)        # list2 : ['apple', 'banana', 'cherry']
print("list3 :",list3)       # list3 : ['apple', 'banana', 'cherry']
print("list4 :",list4)       # list4 : list[slice(None, None, None)]


# SHALLOW SOPY WITH NESTED LITS
       
import copy
list1 = [["apple","banana"],["cherry","mango"]]
list2 = list1.copy()
list1[0][0] = "grape"
print("list1 :",list1)     # list1 : [['grape', 'banana'], ['cherry', 'mango']]
print("list2 :",list2)     # list2 : [['grape', 'banana'], ['cherry', 'mango']]
            
            # Both changed-because inner lists are still shared.

 
# DEEP COPY (Independent copy)
    # If you want a completely independent copy use deepcopy().

import copy
list1 = [["apple","banana"],["cherry","kiwi"]]
list2 = copy.deepcopy(list1)
list1[0][0] = "grapes"
print("list1 :",list1)       # list1 : [['grapes', 'banana'], ['cherry', 'kiwi']]
print("list2 :",list2)       # list2 : [['apple', 'banana'], ['cherry', 'kiwi']]

        # Changes in list1 don't affect list2.