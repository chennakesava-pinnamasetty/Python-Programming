# Simple Word :

   # A global variable can be used any where in your code both inside and outside functions ( if used correctly ).


      # ====  Global variable ====

x = "awesome"
def chenna():
    x = "fantastic" 
chenna()
print("python is "+x+"\n")      # python is awesome


# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

#Create a variable inside a function, with the same name as the global variable
x = "awesome"
def chenna():
    x = "fantsstic"
    print("python is "+x)
chenna()
print("python is "+x+"\n")                    # python is fantsstic
                                             # python is awesome
 

    # === Global Keyword ====

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def chenna():
    global x
    x = "fantastic"
chenna()
print("python is "+x)        # python is fantastic


# ---- Declaring Global Variables Inside a Function.----
      # You can even create a new global variable from inside a function:
def chenna():
    global y
    y = 50

chenna()
print(y)          # 50


# ----  Multiple Globals ----
        # You can declare several at once.
a, b = 1, 2

def change():
    global a, b
    a, b = 10, 20

change()
print(a, b)      # 10 20




#  ====== Why You Should Be Careful ======

        #Using too many globals makes code hard to debug.
        #Functions become dependent on external state.
        #Better alternatives:
        #Pass variables as function arguments.
        #Return values and assign them outside the function.

# ==== Rule of Thumb: ====

    # Use global only when necessary — for example, when writing quick scripts or maintaining state in small programs.
    # In larger projects, avoid it and use parameters/returns.