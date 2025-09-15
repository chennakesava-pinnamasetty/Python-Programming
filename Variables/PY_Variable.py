 # What is a Variable?
    # A variable in Python is just a name that points to a value stored in memory.
    # It’s like a label stuck on a box — the box holds the value, and the label (variable name) lets you find it.


# EX:
x = 10
  # x → variable name (label)
  # 10 → value stored in memory
  # = → assignment operator (assigns the value to the name) 


  
#  CREATING VARIABLES

# ex 1:
x = 5
y = "chenna"
print(x)               # A variable is created the moment you first assign a value to it.
print(y)      


# ex 2:
x = 5
x = "chenna"
print(x+"\n")      # Here only print chenna 

# WHY ?
 # Python is dynamically typed -- this means:
    # You can assign any type of value to a variable and change it later without declaring the type.

# In this code :
  # 1. x = 5   -->   Python stores the integer 5 in variable x.
  # 2. x = "chenna"   -->    Now x no longer holds 4, it holds the sting "chenna".
                            # --->   This is overwrites the old value.
  # 3. print(x) -->   python prints the curret value of x, wchich is "chenna".




                             # ----  CASTING ----

# If you want to specify the data type of variable. This can be done with casting.

a = str(34)                
x = int(1.0)               
y = float(2)               
Y = float(22.000)          
z = complex(5)            
Z = complex(5,9)           

print(repr(a))             #'34'
print(x)                   # 1
print(y)                   #2.0
print(f"{Y:.1f}")          #22.0
print(z)                   #(5+0j)
print(Z,"\n")              #(5+9j)


                                 # ---- GET THE TYPE -----

          # you can get the data type of variable with type() function.

x = 5
y = "chenna"
z = 10j
print(type(x))          # <class 'int'>
print(type(y))          # <class 'str'>
print(type(z),"\n")     # <class 'complex'>




                                # ----  CASE SENSITIVE ----

    # Variable names are case-sensitive.

a = "chenna"
A = "chenna"
print(a)          # chenna
print(A)          # chenna

#A will not overwrite a