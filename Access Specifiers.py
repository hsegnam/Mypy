"""
Python supports 3 access specifiers by using which we can implement emcapsulation and restrict the access of
data members from unauthorized use.
    1. public ---> by default every data member is public by nature
    2. protected data members---> can be aceesed by the class which defines it and its child classes
    3. private ---> These variables can only be used by the class which defines them.

    protected ---->
        Syntax: _varName
    private
        Syntax: __varName
"""
class A:
    def __init__(self):
        self.datapublic = 45
        self._dataProtected = 60
        self.__dataPrivate = 50

    def change(self):
        self.datapublic = 10
        self._dataProtected = 20
        self.__dataPrivate = 30

class B(A):
    def modify(self):
        self.datapublic = 10
        self._dataProtected = 20
        self.__dataPrivate = 30
class C:
    def m1(self):
        print(self._dataProtected)

obj = B()
obj.modify()
print(obj.datapublic)
print(obj._dataProtected)
#print(obj.__dataPrivate)

objC = C()
objC.m1()