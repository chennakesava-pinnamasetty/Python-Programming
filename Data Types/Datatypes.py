# -----  Built-in Standard Data Types -----

         # Python has several categories:
            # a. Text Type
            # b. Numeric Types
            # c. Sequence Types
            # d. Mapping Type
            # e. Set Types
            # f. Boolean Type
            # g. Binary Type
                        
    #----- a. Text Type ----- :
      # str --> Strings
x = "Hello Chenna"


     #---- b. Numeric Types -----
    # int --> Whole numbers
a = 10

    # float --> Decimal numbers
b = 10.5

    # Complex --> Numbers with a real + imaginary part
c = 3 + 5j


    #----- c. Sequence Types -----
     # list --> Ordered, changable, allow duplicates
my_list = [1,2,3]

     # tuple --> Ordered, unchangeable, allow duplicates
my_tuple = (1,2,3)
 
    # range --> Sequence of numbers
r = range(7)  # 0,1,2,3,4


     #----- d. Mapping Type ----- 
     # dict --> Key-value pairs
my_dict = {"name":"Chenna","age":21}


    #---- e. Set Types ----
     # set --> Unordered, no duplicates
my_set = {1,2,3}

     # frozenset --> Immutable version of a set
fset = frozenset({1,2,3})


   #---- f. Boolean Type ----
   # bool --> True or False
is_active = True


  #---- g. Binary Type ----
     # bytes --> Immutable sequence of bytes
b = b"hello"

    # bytearray --> Mutable sequence of bytes
ba = bytearray(5)  # 5 bytes initialized to zero

    # memoryview --> View of bytes without copying
mv = memoryview(b"hello")