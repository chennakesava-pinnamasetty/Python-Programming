
# Escape Character
    # To insert characters that are illegal in a string, use an escape character.
    # An escape character is a backslash \ followed by the character you want to insert.


# in python , we have 10 types of escape charaters.
       # Backslash -->    \\
       # Single quote --> \'
       # Double quote --> \"
       # New line -->     \n
       # Tab -->          \t
       # Carraige Return (line short) --> \r
       # Backspace -->  \b
       # Form Feed -->  \b
       # Octual value --> \000
       # Hepx value --> \xhh


# Backslash
print("a\\b")       # a\b

# Single quote
print("It\'s alright")    # It's alright

# Double quote
print("He said :\"HI\"")   # He said :"HI"

# New line
print("Hello\n World")     # Hello
                           # World

# Tab
print("A\tB")          # A       B

# Carraige Return
print("Hello\rWorld")     # World


# Backspace
print("Hello \bWorld")   # HelloWorld

# Form Feed
print("hello\fworld")      # hello
                           #world

# Octal value
print("\101")             # A

# Hex value
print("\x41")             # a