# Modify strings
   # Python has a set of built-in methods that you can use on strings.

# Upper case
   # The upper() method returns the string in upper case:
a = "chenna kesava"
print(a.upper())         # CHENNA KESAVA


# Lower Case
   # The lower() method returns the string in lower case:
a = "CHENNA KESAVA"
print(a.lower())    # chenna kesava


# Remove Whitespace
    # Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end:
a = "    chenna kesava"
print(a.strip())          # chenna kesava


# Replace String
    # The replace() method replaces a string with another string:
a = "chenna kesava"
print(a.replace('h' , 'z'))       # czenna kesava


# Split String
     # The split() method returns a list where the text between the specified separator becomes the list items.
# The split() method splits the string into substrings if it finds instances of the separator:
a = "chenna, kesava"
print(a.split(","))    # ['chenna', ' kesava']

