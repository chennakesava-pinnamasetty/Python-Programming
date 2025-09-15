# Rules for Variable Names in Python.
      #Python has strict naming rules — break them and you’ll get a SyntaxError.

# Allowed:
    # Letters (a–z, A–Z)

    #Digits (0–9) — but not as the first character.

    #Underscore _ — can be anywhere, even at the start.

# Not Allowed:
     #Spaces (my variable = 5 → Not Allowed )

     #Special symbols like @, $, %, #, etc.

     #Starting with a number (1st_place = "winner" → Not Allowed )


myvar = "Chenna"
my_var = "Chenna"
_my_var = "Chenna"
myVar = "Chenna"
MYVAR = "Chenna"
myvar2 = "Chenna"

print(myvar)         # Chenna
print(my_var)        # Chenna
print(_my_var)       # Chenna
print(myVar)         # Chenna
print(MYVAR)         # Chenna
print(myvar2)        # Chenna


# Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"      #This example will produce an error in the result

 
# Camel Case --  Each word, except the first, starts with a capital letter.
        # myVariableName = "John"

# Pascal Case --  Each word starts with a capital letter.
        # MyVariableName = "John"

# Snake Case --  Each word is separated by an underscore character.
        # my_variable_name = "John"
 
