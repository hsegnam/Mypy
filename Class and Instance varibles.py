'''
Instance variables ---> These are the variables that can only be accessed by class object and class method
    eg. to modify variable value, read
        obj.varName

Class Variables: are also called as static variables
    These variables are maintained and used among all the object of a class
    To access these variables we need to refer them by using class Name
    eg.
        ClassName.ClassVariable


class DemoStaticVar:
    collegeName = "ACS"     # Static or class variable---> it is used commonly by all the objects
    def __init__(self):
        self.RN = None      # instance variable
        self.name = None    # instance variable
    def getData(self,rn,nm):
        self.RN= rn
        self.name = nm
    def display(self):
        print(f'Roll no = {self.RN}\tStudent Name = {self.name}')
        print('College Name = ',DemoStaticVar.collegeName)
obj = DemoStaticVar()
obj.display()
obj.getData(10,'John')
obj.display()
obj2 = DemoStaticVar()
obj3 = DemoStaticVar()
obj4 = DemoStaticVar()
obj2.display()
obj3.display()
obj4.display()
##############################################################################################################

'''

class DemoObjCount:
    count = 0
    def __init__(self):
        DemoObjCount.count= DemoObjCount.count+1
        print(f'Object number {DemoObjCount.count} is created')

o1 = DemoObjCount()
o2 = DemoObjCount()
e = DemoObjCount()
h = DemoObjCount()
g = DemoObjCount()
ob= DemoObjCount()
print('Total Objects Created = ',DemoObjCount.count)