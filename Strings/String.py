
# In python, a string is a sequence of charater enclosed in quotes. 
# It's used to store textual data like words, sentences or even numbers as text.

# CREATING STRING
      # you can create string in 3 types:

# 1. Single quotes
name = 'chenna'

# 2. Double quotes
Greetings = "Hello"

# 3. Triple quotes ( for multi-line )
message = '''Welcome to python''' or """Hello"""



# Strings are Arrays
    # Get the character at position 1 (remember that the first character has the position 0):
a = "Chenna kesava"
print(a[1])    # h


# Loop through the letters in the word " chenna ":
for x in "chenna":
    print(x)   
                   # c
                   # h
                   # e
                   # n
                   # n
                   # a


# String Length
   # o get the length of a string, use the len() function.
a = "chenna kesava"
print(len(a)) # 13


# Check String
    # To check if a certain phrase or character is present in a string, we can use the keyword in.
#ex:
   # Check if "free" is present in the following text:
txt = " The best things in life are free "
print("best" in txt)    # True

# Use it in an if statement:
txt = " The best things in life are free "
if "best" in txt:
    print("yes, 'best' is present")        # yes, 'best' is present


# Check if NOT
    # To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# ex:
txt = " The best things in life are free "
print("expensive" not in txt)      # True

# Use it in an if statement:
# ex:
    # print only if "expensive" is NOT present:
txt = " The best things in life are free "
if "expensive" not in txt:
    print("yes, 'expensive' is NOT present.")  # yes, 'expensive' is NOT present.