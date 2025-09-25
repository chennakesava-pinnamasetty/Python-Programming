
# same method name , different parameters lists (types / numbers).


# Python doesn't support true overealoading at runtime. you simulate it with defaults, *args/**kwargs, type-based dispatch etc..,

# METHOD OVERLOADING :
           # A subclass provides its own implementation of a method that exists in the parent class ( same name & signature).
      # Python : fully supports overriding ( runtime polymorphism).


# 1
'''
class maths:
    def add(self,a,b,c=0):
        return a+b+c
    
m = maths
print(m.add(2,4,5))               # 9
print(m.add(5,6))                  # this get error , because b=0 is not there.

'''

# 2
'''
class maths:
    def add(self,a,b=0,c=0):
        return a+b+c
    
m = maths()
print(m.add(2,3))        # 5
print(m.add(1))          # 1

'''


# 3
'''
class maths:
    def add(self,a,b=0,c=0):
        return a+b-c

m = maths()
print(m.add(1,2,3))        # 0
print(m.add(2,4,7))        # -1

'''



# ANOTHER WAY TO CALCULATE
       
       # *args

'''
class maths:
    def add(self,*args):
        return sum(args)
    
m = maths()
print(m.add(2,4,5))                     # 11
print(m.add(2,4,5,6,7,8,9))             # 41
print(m.add(1,2,3,4,5,6,7,8,9))         # 45
print(m.add(9,8,7,6,5,4,3,2,1,9))       # 54

'''