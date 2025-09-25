'''class car:
    brand = "toyato"
    color = "green"            # this is without object

    def drive(self):
        print("car is moving")

my_car = car()
my_car.drive()'''



# Two examples display and own one
# 1.

'''class car:
    def __init__(self,brand,color):           # __init__ (constructor) work , when a object created,and  self refers to the current object.

        self.brand = brand
        self.color = color

    def display (self):          # here we taken only display 
        print(f"the car brand is '{self.brand}' and color is '{self.color}'")
 
my_car = car("toyato","green")     # this is object

my_car.display()'''               # we want to output , we should write this.


  
  # another Example :
# 2.
'''
class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color =  color

    def another (self):
        print(f"the car barnd is '{self.brand}' and color is '{self.color}'")

my_car = car("totato","green")
my_car.another()                         # the car barnd is 'toyato' and color is 'green'

                                                       here, i take a random name and it works


          # ( Or ) 
# we take print(my_car)
print(my_car)    '''               # <__main__.car object at 0x000002071C0F1DC0>    only came, because, we didn't use __str__ , that why this came human-unreadable




# Now we take __str__  
      # This one is convert that human-readable version :
'''
class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    
    def __str__(self):
        return f"the car barnd is '{self.brand}' and color is '{self.color}'"

my_car = car("toyato","green")
print(my_car)'''
                              # the car barnd is 'toyato' and color is 'green'








 # Attributes ( Variables in a class)
'''
class dog:
    species = "mammmal"

    def __init__(self,name,age):
        self.name = name
        self.age = age

dog1 = dog("tommy",1)
dog2 = dog("bruno",3)

print(dog1.name, dog1.age, dog1.species)  # tommy 1 mammmal
print(dog2.name, dog2.age, dog2.species)  # bruno 3 mammmal
'''



# Methods in a class
'''
# 1. Instance methodds
class methods:
    def square(self, x):
        return x*x

#Class method
    @classmethod
    def cube(cls,x):
     return x*x*x

#ststic method
    @staticmethod
    def add(a,b):
       return a+b

obj = methods()
print(obj.square(6))

print(methods.cube(3))
print(methods.add(5,8))'''



# Diff b/w __str__ and __repr__
'''
class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    
    def __str__(self):
        return f"the brand is {self.brand} and the color is {self.color}"            # the brand is tesla and the color is green

    def __repr__(self):
        return f"the brand is {self.brand} and the color is {self.color}"           # the brand is tesla and the color is green
    
c1 = car("tesla","green")
print(c1)   # This one automatically calls __str__
print(repr(c1))   # But this one, we manually write the method'''












# own  Work
'''
class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def action(self,km):
        self.km = km
        print(f"The car brand is {self.brand}, color is {self.color} and km is {self.km}")
    
    def mod(self,modell):
        self.modell = modell      # # save model permanently
        print(f"The car brand is {self.brand}, color is {self.color}, km is {self.km} and model is {self.modell}")

    def sp (self,speed):
        print(f"The car brand is {self.brand}, color is {self.color}, km is {self.km} and model is {self.modell} , the speed is {speed}")

c1 = car("Toyato","green")
c1.action(" 45 km/h")
c1.mod("Tesla")
c1.sp("100 km")


out put :

The car brand is Toyato, color is green and km is  45 km/h
The car brand is Toyato, color is green, km is  45 km/h and model is Tesla
The car brand is Toyato, color is green, km is  45 km/h and model is Tesla , the speed is 100 km '''





# same concet but diff

'''
class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def action(self,km):
        print(f"car brand {self.brand}, color {self.color} and km {km}")
 
    def mod(self,km,model):                                                                         # Pass km  in mod()
        print(f"car brand {self.brand}, color {self.color}, km {km} and model {model}")             

    def sp(self,km,model,speed):                                                                    # Pass km,model again in sp()
        print(f"car brand {self.brand}, color {self.color}, km {km} , model {model} and speed is {speed}")

c1 = car("Toyato","green")
c1.action("120 km")
c1.mod(60,"theledu")
c1.sp(45,"tesla","45 km/h")

    
car brand Toyato, color green and km 120 km
car brand Toyato, color green, km 60 and model theledu
car brand Toyato, color green, km 45 , model tesla and speed is 45 km/h
'''



class Car:
    def __init__(self, brand, model):  # constructor
        self.brand = brand
        self.model = model
        print("Car object created!")

    def deta(self):  # normal method
        return f"{self.brand} {self.model}"

c1 = Car("Toyota", "Fortuner")   # __init__ runs automatically
print(c1.deta())              # normal method called manually
