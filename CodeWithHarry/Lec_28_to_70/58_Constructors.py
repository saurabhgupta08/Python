# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

# Types of Constructors in Python
# 1)Parameterized Constructor
# 2)Default Constructor
# Parameterized Constructor in Python
# When the constructor accepts arguments along with self, it is known as parameterized constructor.
# These arguments can be used inside the class to assign the values to the data members.

# Default Constructor in Python
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.

class person:
    def __init__(self,name,occ):
        self.name=name             #Constructor
        self.occ=occ


    def info(self):
        print(f"{self.name} is {self.occ} ")

a=person("Saurabh Gupta","traveller")
name=input("Enter your name sir ")
occ=input("Enter yooccupation ")
b=person(name,occ)
c=person("Nishant Gupta" ,"Businessman")

a.info()
b.info()
c.info()