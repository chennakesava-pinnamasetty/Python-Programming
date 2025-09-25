
# What is Multiple Inheritance?
 
# Inheritance = When a class (child) can use the properties and methods of another class (parent).

# Multiple inheritance = When a class inherits from more than one parent class.

# 1

'''
class parent:
    def skills(self):
        print("this is parent class")

class mother:
    def skills(self):
        print("This is mother class")

class child(parent,mother):
    def skills(self):
        parent.skills(self)
        mother.skills(self)
        print("this is child class")

c = child()
c.skills()
                        # this is parent class
                        # This is mother class
                        # this is child class

                        '''
# 2

'''
class father:
    def skills(self,name,age):
        self.name = name
        self.age = age
        print(f"name {self.name} and age {self.age}")
        
class mother(father):
    def skills(self,name,age,gender):
        father.skills(self,name,age)
        self.gender = gender
        print(f"name {self.name} , age {self.age} and gender {self.gender}")

class child(mother):
    def skills(self,name,age,gender,year):
        mother.skills(self,name,age,gender)
        self.year = year
        print(f"name {self.name} , age {self.age} , gender {self.gender} and year {self.year}")

c = child()
c.skills("chenna",21,"male",2022)
   

 # name chenna and age 21
 # name chenna , age 21 and gender male
 # name chenna , age 21 , gender male and year 2022

 '''