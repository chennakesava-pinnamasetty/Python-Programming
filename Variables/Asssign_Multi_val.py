# Here some types of assign multi values 

# ---- 1. Multi Variable Assign Multi Values ----
               # you can assign multiple variables in one line.

a,b,c = 1,2,3
print(a)          # 1
print(b)          # 2
print(c,"\n")     # 3


# ---- 2. Multiple Variables, Some values ----

x = y = z = 200
print(x)            # 200
print(y)            # 200
print(z,"\n")       # 200


# ---- 3. Swapping values ( without temp variable )

a,b = 4,8
a,b = b,a
print(a)
print(b,"\n")


# ---- 4. Unpacking Collections ----
    # you can assign values from list, tuple, or string directly.

fruits = ["apple","banana","cherry"]
f1,f2,f3 = fruits
print(f1)            # apple
print(f2)            # banana
print(f3,"\n")       # cherry


# ---- 5. Using * for extra values ----
      # if you don't know how many values there are, use * catch the rest.

numbers = [1,2,3,4,5,6,7]
a,b, *rest = numbers
print(a)              # 1
print(b)              # 2
print(rest,"\n")      # [3,4,5,6,7]

# ( or )
*a,b,c = numbers
print(a)         # [1,2,3,4,5]
print(b)         # 6
print(c,"\n")    # 7


# ---- 6. partial Unpacking ----

a,_,c = [10,20,30]          # '_' means "ignore this value".
print(a,c)    # 10,30


