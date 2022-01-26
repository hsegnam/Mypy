'''
Inheritance : it is the mechanism of creating new class from existing one,
    so that the newly created class can inherit and use the menbers of existing class.
old class from which we create the new one is called as ---> Base class     /Parent class/Super Class
and newly created class is called as --->                    Derived class  /child class / sub class
syntax:
        class Parent:
            parent data and methods

        class Child(Parent):
            data and methods of child


Python supports 5 types of inheritance:
    Single
    Multilevel
    Multiple
    Hierachycal
    Hybrid


# Single inheritance
class A:
    def __init__(self):
        self.varA = 10

    def m1(self):
        print('This is method of class A')

class B(A):
    def __init__(self):
        self.varB = 20

    def m2(self):
        print('this is class B derived from class A')

obj = B()
print(obj.varB)
print(obj.varA)
obj.m1()
obj.m2()


#########################################################################################
# Miltilevel Inheritance
class A:
    def m1(self):
        print('This is method 1 form class A')

class B(A):
    def m2(self):
        print('This is method 2 from class B')

class C(B):
    def m3(self):
        print('This is method 3 from class C')

class D(C):
    def m4(self):
        self.m1()
        self.m2()
        self.m3()
        print('This is method 4 from class D')

objD = D()
objD.m4()


#########################################################################################
# Multiple inheritance
class A:
    def m1(self):
        print('From Class A')

class B:
    def m2(self):
        print('From B')
class C:
    def m3(self):
        print('From C')

class D(A,B,C): # class D is having three parents namely class A, Class B, class C
    def m4(self):
        print('From class D')
        self.m1()
        self.m2()
        self.m3()
objD = D()
objD.m4()
objD.m1()

####################################################################################################################

# Hierachycal inheritance

class A:
    def m1(self):
        self.a = 10
        print('this is method from class A')
class B(A):
    def m2(self):
        print("This is method of class B")
class C(A):
    def m3(self):
        print('This is method from class C')
# we have created the child classes from A---> class B and  class C

objB = B()
objC = C()
objB.m2()
objB.m1()
#print(objC.a)
#print(objB.a)
objC.m1()
objC.m3()



################################################################################################################################

#Hybrid inheritance


class A:
    def m1(self):
        self.a = 10
        print('this is method from class A')
class B:
    def m2(self):
        print("This is method of class B")
class C(A,B):
    def m3(self):
        print('This is method from class C')
# we have created the child classes from A---> class B and  class C
class E(C):
    pass
class F(C):
    def m6(self):
        print('This is class F created from class C')

objB = B()
objC = C()
objB.m2()
#print(objC.a)
#print(objB.a)
objC.m1()
objC.m3()

objF= F()
objF.m1()
'''


class A(object):
    def __init__(self):
        self.name = 'Bunty'
    def m1(self):
        self.college = 'ACS'
class B():
    def __init__(self, roll):
        A.m1(self)
        A.__init__(self)
        self.roll = roll

object = B(23)
print(object.name)
print(object.college)
