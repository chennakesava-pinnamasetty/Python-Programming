

# Operator Overloading:

          # Python supports operator overloading by defining special methods (also called magic methods or dunder methods) in classes. 
                    # For example, you can define how the + operator works for your custom objects by implementing the __add__ method.



# __add__       +
# __sub__       -
# __mul__       *
# __truediv__   /
# __eq__        ==
# __it__        <
# __le__        <=



# 1

class Box:
    def __init__(self,volume):
        self.volume = volume

    def __eq__(self,other):
        return self.volume == other.volume
    
    def __lt__(self,other):
        return self.volume < other.volume
    
b1 = Box(10)
b2 = Box(20)

print(b1 == b2)
print(b1 < b2)



