
# ADD SET ITEMS

      # Once a set is created, you cannot change its items.   but you can add new items.

# In Two main methods :
     # 1. add
     # 2. update


# 1. add :  
            # For single items.

fruits = {"apple","banana","cherry"}
fruits.add("orange")
print(fruits)             # {'banana', 'apple', 'cherry', 'orange'}



# UPDATE :
              # For multiple items.

fruits = {"apple","banana","cherry"}
tropical = {"pineapple","mango","orange"}
fruits.update(tropical)
print(fruits)                  # {'cherry', 'orange', 'pineapple', 'apple', 'mango', 'banana'}



# NOTES :

       # Duplicates values are ignored automatically.
       # Order is not fixed, so new items may appear in any position when printed.