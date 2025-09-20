
# SORT LISTS
        # Sorting in lists means arranging the items in a particular order
     # -- usually ascending (smallest to largest) or descending(largest to smallest).

# In python, there are two main ways to sort a list.

# 1. Sort() method
        # Changess the list in place(modifies the original list).

numbers = [5,2,9,1]
numbers.sort()
print(numbers)         # [1, 2, 5, 9]

numbers.sort(reverse = True)
print(numbers)      # [9, 5, 2, 1]


# Sorted() function
       # Returns a new sorted list, Leaving the original list unchanged.

numbers = [5,2,9,1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)      # [1, 2, 5, 9]

desc_sorted = sorted(numbers,reverse=True)
print(desc_sorted)       # [9, 5, 2, 1]


# DIFFERENCE B/W sort() and sorted()
      # sort() = Changes the original list.
      # sorted() = creates a new sorted list.


# Reverse order
Thislist = ["banana","orange","kiwi","cherry"]
Thislist.reverse()
print(Thislist)         # ['cherry', 'kiwi', 'orange', 'banana']

