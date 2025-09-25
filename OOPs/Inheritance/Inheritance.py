# Inheritance is a feature of oop where one class (child / derived class) can use the properties & methods of another class ( parent / base class ).

# basic example:

# 1
'''
class animal:
    def sound(self):
        print("animals make sounds")

    def sound(self):
        print("dogs barks")

a = animal()
a.sound()  '''       # dogs barks


# 2
'''
class animal:
    def sound(self):
        print("animals makes sound")

    def sound1(self):
        print("dog braks")

a = animal()
a.sound()         # animals makes sound
a.sound1()       # dog braks  '''


# 3
'''
class animal:
    def sound(self):
        print("animal makes sound")

    def sound1(self):
        self.sound()
        print("dogs braks")

a = animal()
a.sound1()  '''            # animal makes sound 
                           # dogs braks


# super class
# 4
'''
class animal:
    def sound(self):
        print("animals make sounds")

class animal1(animal):
    def sound(self):
        super().sound()
        print("dogbraks")

a = animal1()             
a.sound()'''                  # animals make sounds 
                           # dogbraks

                      # explicit call parent method, it takes the parent and defined method , it works like super class
# explicit
# 5
'''
class animal:
    def sound(self):
        print("animal make sound")

class animal1(animal):
    def sound(self):
        animal.sound(self)
        print("dog braks")

a = animal1()
a.sound()'''                     # animal make sound
                            # dog braks




'''
class animal:
    def sound(self):
        print("animal makes sounds")

class animal1(animal):
    def works(self):
        super().sound()
        print("dog braks")

a = animal1()
a.works()'''        # animal makes sounds
                    # dog braks

                             # it takes diff methods also.





                