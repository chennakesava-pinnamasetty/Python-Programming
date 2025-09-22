
# LOOP TUPLES

# 1. Using for loop (direct access)
         # You can loop directly through each item in the tuple.

fruits = ("apple","banana","cherry")
for x in fruits:
    print(x)          # apple
                      # banana
                      # cherry


# 2. Using for loop with index
          # You can also use range() and keys() to loop using indexes.

fruits = ("apple","banana","cherry")
for x in range(len(fruits)):
    print(f"{x} ->",fruits[x])          # 0 -> apple
                                        # 1 -> banana
                                        # 2 -> cherry


# 3. While loop
          # You can use a while loop for more control.

fruits = ("apple","banana","cherry")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1           # apple
                     # banana
                     # cherry
                     