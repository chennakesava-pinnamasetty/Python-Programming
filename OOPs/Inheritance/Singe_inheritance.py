
# single inheritance  -->  one parent, one child

                  # Single Inheritance = When a child class inherits from only one parent class.


# 1
'''
class parent:
    def sound(self):
        print("hello from parent")

class child(parent):
    def voice(self):
       print("hello from child")

a = child()
a.voice()'''           # hello from child



# 2
'''
class parent:
    def sound(self):
        print("hello from parent")

class child(parent):
    def voice(self):
        print("hello from child")

a = child()
a.sound()             # hello from parent
a.voice()'''          # hello from child


# 3
'''
class parent:
    def sound(self):
        print("hello from parent")

class child(parent):
    def voice(self):
        super().sound()
        print("hello from child")

a = child()
a.voice()'''             # hello from parent
                         # hello from child


'''
class parent:
    def sound(self):
        print("hello from parent")

class child(parent):
    def voice(self):
        parent.sound(self)
        print("hello from child")

a = child()
a.voice()'''                # hello from parent
                          # hello from child



# calculation
'''
class calculation:              # parent
    def add(self,a,b):
        return a + b
    def sub (self,a,b):
        return a - b
    
class yento(calculation):      # child
    def mul (self,a,b):
        return a * b
    def div (self,a,b):
        if b != 0  :
            return a / b
        else:
            print("invalid")

yem = yento()

print("add :",yem.add(5,3))
print("sub :",yem.sub(5,3))
print("mul :",yem.mul(5,3))
print("div :",yem.div(5,3))'''





class parent:
    def voice(self,name,age):
        self.name = age
        self.age = age
        print(f"your parent name {name} and age is {age}")

class child(parent):
    def sound(self,name,age):
        parent.voice(self,name,age)
        print(f"your child name {name} and age is {age} ")

a = child()
a.sound("chenna",21)                        # your parent name chenna and age is 21
                                            # your child name chenna and age is 21