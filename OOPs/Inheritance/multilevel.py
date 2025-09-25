
'''
class grandfather:
    def voice(self,age,name):
        print(f"grandfather name is '{name}' and age is '{age}'")

class parent(grandfather):
    def noise(self,name,age):
        print(f"you parent name is '{name}' and age is '{age}' ")

class child(parent):
    def sound(self,name,age):
        print(f"your child name is {name} and age is '{age}' ")
        

a = child()
a.voice("chenna",21)                    # grandfather name is '21' and age is 'chenna'
a.noise("kesava",25)                    # you parent name is 'kesava' and age is '25' 
a.sound("reddy",29)'''                 # your child name is reddy and age is '29'
    


'''
class grandfather:
    def first(self,name,age):
        print(f"grandfather name is {name} and age is {age}")

class parent(grandfather):
    def second(self,name,age):
        grandfather.first(self,name,age)
        print(f"parent name is {name} and age is {age}")

class child(parent):
    def third(self,name,age):
        parent.second(self,name,age)
        print(f"child name is {name} and age is {age}")

a = child()
a.third("chenna",21)'''                      # grandfather name is chenna and age is 21
                                          # parent name is chenna and age is 21
                                          # child name is chenna and age is 21





class student:
    def __init__(self,name):
        self.name = name

    def __str__ (self):
        return f"your name {self.name}"
    
class marks(student):
    def __init__(self,name,marks):
        self.marks = marks
        super().__init__(name)

    def  __str__(self):
        return f"your marks {self.marks}"
    
class grade(marks):
    def __init__(self,name,marks):
        super().__init__(name,marks)

    def calculation(self):
        if self.marks >= 90:
            return "a"
        elif self.marks >= 75:
            return "b"
        elif self.marks > 50:
            return "c"
        else:
            print("fail")


a = grade("chenna",78)
print(a)
print("grade:",a.calculation())


