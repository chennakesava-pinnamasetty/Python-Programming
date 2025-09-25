

# METHOD OVERRIDING :

     # Method overriding occurs when a subclass  provides a specific implementation of a method that is already defined in its parent (super) class.
     #  The subclass method replaces or extends the behavior of the parent class method.


# 1

'''
class parent:
    def sound(self):
        print("I am parent")

class child:
    def sound(self):
        #parent().sound()
        print("Iam the child")

c = child()        # I am parent
c1 = parent()

c.sound()
c1.sound()           # Iam the child
                     # I am parent

'''



# 2

'''
class parent:
    def sound(self):
        print("I am the parent class")

class child:
    def sound(self):
        parent().sound()
        print("I am the child")

p = child()
p.sound()                        # I am the parent class
                                 # I am the child
'''