'''
Classes and objects
    To create an object we must define its structure or blueprint by using the class
    and when we create the variables of this class is it called as an object
syntax of class:

class className:
    # Data members
    .
    .
    .
    memberFunctions()
    .
    .
    .

To ctreate the object

objectName = className()



class Addition:

    def add(self,x,y):
        self.num1 = x
        self.num2 = y
        return self.num1+self.num2

obj1 = Addition()
res = obj1.add(4,7)
print('Num1 = ', obj1.num1)
print('Num2= ',obj1.num2)
print('Addition = ', res)

'''

class Student:
    def getData(self):
        self.RN = int(input('Enter the Roll num: '))
        self.name = input('Enter the name: ')
        self.dob = input('Enter the date of birth: ')
        self.email = input('Enter the email address: ')
        self.mob = int(input('Enter the mob No: '))
    def showData(self):
        print(f'Roll no: {self.RN}\nName: {self.name}\nDate od Birth: {self.dob}\nEmail: {self.email}\nMobile: {self.mob}')

stud1 = Student()
stud1.getData()
stud1.showData()

stud2 = Student()
stud2.RN=5
stud2.name="Jill"
stud2.dob = "02/05/1994"
stud2.email = "jill@gmail.com"
stud2.mob = 3214569870

stud2.showData()
print(stud2.RN)
print(stud2.name)
