
# Concatenation in Python simply means joining things together.
# Most often, it’s used for joining strings.


#  String Concatenation
      # To concatenate, or combine, two strings you can use the + operator.
a = "chenna"
b= "kesava"
c = a + b
print(c)        # chennakesava


# ex:
    # To add a space between them, add a " ":
a = "chenna"
b = "kesava"
c = a +" "+b
print(c)            # chenna kesava


#  Using += for concatenation
a = "chenna"
a += "kesava"
print(a)         # chennakesava 


# convert numbers to strings:
age = 25
print("i am "+str(age) + " years old")    # i am 25 years old