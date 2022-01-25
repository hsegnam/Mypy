'''
Constructor is a method that is immidiately invoked or called as soon as the object of the class is created
     Basically is is used to initialize the variables.
     Constructor is defined by using __init__() method
     We can have two types of constructors
        1. Default constructor
        2. Parameterized Constructor
Syntax :
        def __init__(self, argument_list):
            statements


#################################################################################
class demoConstructor:
    def __init__(self):
        print('This is Constructor. It is called automatically when object is created')

obj1 = demoConstructor()

#################################################################################
# Default Constructor
class add:
    def __init__(s):
        s.a=0
        s.b=0

    def accept(self):
        self.a = int(input('Enter a: '))
        self.b = int(input('Enter b: '))

    def display(self):
        print(f'a= {self.a} b= {self.b}')
        print('Addition = ',(self.a+self.b))

obj1 = add()
print('Variables initialized by the constructor are:')
obj1.display()
obj1.accept()
obj1.display()

################################################################################



# Parameterized Constructor ---> The constructor that can accept the values through parameters

class DemoParaConstr:
    def __init__(self,x,y):
        self.a = x
        self.b = y

    def accept(self,p,q):
        self.a = p
        self.b = q

    def show(self):
        print(f'a= {self.a}\tb= {self.b}')
        print('Addition = ',(self.a+self.b))

obj2 = DemoParaConstr(2,3)
obj2.show()
obj2.accept(5,9)
obj2.show()

'''

class Student:
    def __init__(self,rn,name):
        self.RN = rn
        self.name =name
        self.collegeName = None
        self.dob = None
        self.Email = None
        self.percentages = 0.0

    def showData(self):
        print(f'Roll No ={self.RN}\nName = {self.name}\nCollage Name = {self.collegeName}\nBirth Date ={self.dob}\nEmail Id = {self.Email}\nPercentages = {self.percentages}')

obj = Student(9,'Jack')
obj.showData()
obj.collegeName = "ACS"
obj.dob = '01/01/2000'
obj.Email = 'jack@gmail.com'
obj.percentages = 56
obj.showData()
