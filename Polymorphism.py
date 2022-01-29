'''
Polymorphism means one mane with many duties, the word polymorphism is made up of 2 words:
        1. Poly ---> Many
        2. Morphs ---> Forms
So in any OOP language it is possible to provide multiple meaning to the same funtion and this property is known as
    Polymorphism
Polymorphism is achieved by two ways:
    Function Overlaoding ---> Same class with multiple functions defined with the same name ---> not sopported by python
    Function Overriding --->  different inherited classes having mthods with same name

# Built in example of polymorphism

# 1. plus operator ---> can be used to addition of numbers as well as concatenation

a=20
b=30
print(a+b) # Addition of numbers(int, float, complex)

str1 = "Python"
str2 = 'Programming'
print(str1+" "+str2)

list1 = [1,3,4]
list2 = [5,6,7]
list3 = list1+list2
print(list3)
#####################################################################################################
# C++ Method Overloading
#include <iostream>
using namespace std;
class A
{
    public:
    int a,b;

    public:

    void m1()
    {
        cout<<"This is First m1\n";
    }

    void m1(char *x)
    {
        cout<<"This is second m1 welcome"<<x<<"\n";
    }

    void m1(int a)
    {
        cout<<"This is third m1 "<< a<<"\n";
    }

};

int main()
{
A obj;
obj.m1(2);
obj.m1(" To Python");
obj.m1();
}



#####################################################################################################

class A:
    def m1(self):
        print('This is first m1() in class A')

    def m1(self,msg):
        print("This is second m1() welcome",msg)

obj = A()
obj.m1()
obj.m1(' to Python')

# Note: Method overloading is not supported by Python

###########################################################################################################

'''

# Method Overriding:
# To call the base os parent class method we use super method
class A:
    def m1(self):
        print('This is first m1() in class A')

    def m2(self):
        print('This is first m2() in class A')


class B(A):
    def m1(self,msg):
        #o = A()
        #super().__init__()
        super().m1()
        print("This is second m1() in class B welcome",msg)

objB = B()
#objB.m1(' to Python')
objB.m2()
objB.m1(' to Python')
