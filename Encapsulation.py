'''
Encapsulation is the mechanism that binds data members and member functions together in a class.
It basically provives the security to the data and it is also possible to restrict the access of data members
by using encapsulation.
We can restrict the varible access by making them either
    protected ---->
        Syntax: _varName
    private
        Syntax: __varName
'''

class DemoEncapsulation:
    def __init__(self):
        self.var1 = 0
        self.__var2 = 10

    def method1(self):
        print('public value = ',self.var1)
        print("Private Value",self.__var2)

obj = DemoEncapsulation()
obj.method1()
print('Outside the class value1 = ',obj.var1)
print('Outside the class Value 2 = ',obj.__var2)