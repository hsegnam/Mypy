'''
Function is a block of code organized under a single name.
It is defined in order to do a specific task
 Syntac :
def FunName(Arguments):
    ststements
    return

The function is used by calling it
to call a function we just type the mane of function and provide the number agruments in paranthesis

FunName(arguments)

'''
'''
#- find the list of length of each string in the given list

list1 = ['Python', 'Java', 'Example','This is the list', 'That\'s it']

def callen(lst):
    lst1 = []
    for i in lst:
        lst1.append(len(i))
    return lst1

resList = callen(list1)

print('The list of length of each string in the given list is:',resList)



# - Python progam to reverse the given number 123---> 321

def rev(n):
    rev = 0
    while(n>0):
        rev = rev*10 + n%10 # 123--> 0+3*10--> 30
        n = n//10 # 12
    return rev

no = int(input("Enter a number"))
res = rev(no)
print(f'Original Number: {no} and\nreversed Number : {res}')
'''

# - pp to find the sum of digits in number

'''
Function parameters
    1. Positional Parameters ---> position wise arguments are taken
    2. Default Parameters---> positional but we can assign default values to then
    3. Variable Length Paramaters ---> Here the number of parameters are not fix and we can five any number of 
        arguments to the function 
    4. Keyword Parameters ----> Parameters are provoded in the form of name=Value manner while calling
    5. Varible Length Keyword paramaters ---> Here the number of parameters are notfix and we can five any number of 
        arguments to the function 

# Posotional parameters

def add(a,b):
    c = a+b
    return c

res = add(20,30)
print(res)

# Default parameter

def stud(rn,name,email='NA', mob = None):
    print('Student Deatails: ')
    print(f'Roll No: {rn}\nName: {name}\nEmail: {email}\nMobile:{mob}')
stud(10,'Monty','Monty@gmail.com',1234567890)
stud(11,'Minty')



# Variable Length argunments
# def funName(*args):
def demoVarlen(*args):
    print('Total arguments received are: ',len(args))
    add =0
    for i in args:
        add = add+i
    return add
tot = demoVarlen(1,5,100,23,5,3,7,8,85,256,8,3,6,8,9,4,2,7,8)
print(tot)



# Keyword Parameter
def demokeyword(name="", age=0 ,mob=0):
    print(f'Name: {name}\nAge: {age}\nMobile: {mob}')

demokeyword(name='John',age='32',mob=1236547890)
demokeyword(mob=3214569870,name='Python',age=30)

'''

# Variable Length Keyword parameter
# def funName(**kwargs)

def demovarkeyword(**kwargs):
    for i in kwargs:
        print(kwargs[i])

demovarkeyword(name="Function",typesn=5,lang='Python', date='18/01/2022')
