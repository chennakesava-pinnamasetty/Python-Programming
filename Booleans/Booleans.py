
# BOOLEANS
    # Booleans represents one of two values True or False
     # These are used in logical, conditional and comaprisions.

# TYPE
x = True
y = False
print(type(x))  # <class 'bool'>

# COMPARISION
print(10 > 5)     # True
print(5 > 10)     # False
print(10 == 10)   # True


# CONDITIONAL STSTEMENTS
age = int(input("Enter your age : "))
if age >= 18:
    print(f"yes, age is {age} your eligible")
else:
    print("no, your not eligible")       # yes, age is 25 your eligible




# Boolean values of Diff data types:

     # almost any value is evaluted to True, if it has some sort of content.
     # Any string is True, except empty strings.
     # Any number is True, except 0.
     # Any list,set and Dictionary are True, except empty ones.

print(bool(0))       # False
print(bool(0.0))     # False
print(bool(""))       # False
print(bool([]))       # False
print(bool(()))       # False
print(bool({}))       # False
print(bool(None))     # False


print(bool(10))           # True
print(bool(-5))           # True
print(bool(3.14))         # True
print(bool("hello"))      # True
print(bool([1,2,3]))      # True
print(bool((10)))         # True
print(bool({"a":1}))      # True
print(bool(" "))          # True

