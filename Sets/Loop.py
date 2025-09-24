
# LOOP SETS

      # You can loop through the set items by using for a loop.


# 1. BASIC LOOP

fruits = {"apple","banana","cherry"}
for i in fruits:
    print(i)         # banana 
                     # apple
                    # cherry 


# 2. LOOP WITH INDEX (using enumerate)

fruits = {"apple","banana","cherry"}
for i,n in enumerate(fruits):
    print(i,"->",n)                # 0 -> banana
                                   # 1 -> cherry
                                   # 2 -> apple


# 3. LOOP AFTER SORTING
          # If you want to loop in a sorted order:

fruits = {"banana","apple","banana","cherry"}
for i in sorted(fruits):
    print(i)          # apple
                      # banana
                      # cherry


        # Now, it will print in aplhabetical order.