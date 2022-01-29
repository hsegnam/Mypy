'''
class A:
    def __init__(self):
        self.x = 10
    def m1(self):
        self.y = 20

class B(A):
    def __init__(self):
        A.__init__(self)
        A.m1(self)
        self.z=30

objB = B()
print(objB.x)
print(objB.y)

###################################################################################################################

Instance method, Class Method and Static method

Instance method: These are instance or object specific methods, means these methods cannot be used without creating
                    the object. Every class method must be provided with self object while defining the method

Class method: Class method is class specific method. so in order to use it we must prefix it with the class name.
                It recieves cls as a compulsory argument, so that is can use class variables
                These can work as an additional constructor.
                These methods are used in order to write factory methods
                @classmethod decorator is used to define a class method

Static method: Static methods are not class or instance specific so these methods are not able to use oe modify the class data
                or class state. These methods can be invoked by using oject or class name
                These methods are used to write some utility functions.
                @staticmethod decorator is used to define a static method



class DemoMethods:
    def m1(self):
        print('This is the Instance method')

    @classmethod
    def m2(cls):
        print('This is the Class method')

    @staticmethod
    def m3():
        print('This is the Static method')

obj = DemoMethods()
obj.m1()
obj.m2() # calling class method by using object
obj.m3() # calling static method by using object

DemoMethods.m1(obj) # Calling instance method by using class name
DemoMethods.m2()    # Calling class method by using class name
DemoMethods.m3()    # Calling static method by using class name


###############################################################################################################


class DemoMethods:
    company = 'ABC ltd'
    def __init__(self,id,nm):
        self.eid = id
        self.name = nm
        print('Company: ',DemoMethods.company)

    def display(self):
        print(f'Employee id: {self.eid}\nEmployee Name: {self.name}\nCompany Name: {DemoMethods.company}')

    @classmethod
    def m1(cls):
        cls.company = "PQR ltd"
        #print('New company',cls.company)

    @classmethod
    def altconctructor(cls,newid,newname):
        return cls(newid,newname)

    @staticmethod
    def chkname(name):
        if(name.isalpha()):
            print('Valid Name')
        else:
            print('Invalid name')

obj= DemoMethods(101,'John')
obj.display()
DemoMethods.chkname(obj.name)
obj.m1()
obj = DemoMethods.altconctructor(102,'Johny1')
obj.display()
DemoMethods.chkname(obj.name)

##############################################################################################################

'''

# We need to generate Student result----> Student basic details---> Exam will give us the marks ----> we have show result

class Student:
    def getStudInfo(self):
        self.name = input('Enter the name: ')
        self.rollN = int(input('Enter Roll No: '))
        self.DOB = input('Enter the Birthdate: ')
        self.email = input('Enter the email address: ')
        self.mob = int(input('Enter the mob: '))

    def displayBasicInfo(self):
        print(f"Roll NO: {self.rollN}\t\t\tName: {self.name}")
class Marks(Student):
    def inputMarks(self):
        self.marathi = int(input("Enter Marathi Marks: "))
        self.english = int(input("Enter English Marks: "))
        self.hindi = int(input("Enter Hindi Marks: "))

    def displayMarks(self):
        print('Marathi: \t\t\t\t',self.marathi)
        print('English: \t\t\t\t', self.english)
        print('Hindi: \t\t\t\t\t', self.hindi)

class Result(Marks):
    def calculate(self):
        self.per = (self.hindi+self.english+self.marathi)/3
    def showClass(self):
        pass # You have to write it by your own

    def displayResult(self):
        self.displayBasicInfo()
        self.displayMarks()
        print('Percentages: \t\t\t',self.per)

s1 = Result()
s1.getStudInfo()
s1.inputMarks()
s1.calculate()
s1.displayResult()