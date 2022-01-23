'''
- Lambda Function is a just in time function
- Which is very similar to inline function in c++
- anonymous function
Syntax:   variableName = lambda arguments: Expression

varName(arguments)


add = lambda a,b: a+b

print(add(5,8))



x = lambda m,n: m>n
print(x(2,3))

################################################################################################


# map() function----> map function can be used to  apply and map a function over an iterable


#- find the list of length of each string in the given list

lst1 = ['This', 'is','the','Python','Programming','Language']
#lst2 = list(map(fun,listVariable))
def lislen(l):
    ls=[]
    for i in l:
        ls.append(len(i))
    print(ls)
lislen(lst1)

#- find the list of length of each string in the given list by using map() and simple function
def strl(s):
    return len(s)

l = strl('Python')
print(l)

lst1 = ['This', 'is','the','Python','Programming','Language']

lst2 = list(map(strl,lst1))
print(lst1)
print(lst2)



lst1 = ['This', 'was','the','Python','Programming','Language','which','is','awesome']
#- find the list of length of each string in the given list by using map() and lambda function

list3 = list(map(lambda s: len(s),lst1))
print(lst1)
print(list3)



# concartenate 2 numbers and generate the third one by using lambda function

num3 = lambda num1,num2: int(str(num1)+str(num2))
res = num3(3,7)
print(res)
print(type(res))


# filter()---> is used to apply a filter function on an iterable

def eve(n):
    if n%2==0:
        return n

list4 = list(range(1,11))
print(list4)

list5 = list(filter(eve,list4))
print(list5)



list4 = list(range(1,11))
print(list4)

list5 = list(filter(lambda num:num%2==0,list4))
print(list5)

######################################################################

# Decorators----> it is used to add the functionality to an existing function
# Decorator recieves function as an agrument to which it applies additional functionalities
def message(s):
    print(s)
print('******************************************************************')
message("Hello World!")
print('******************************************************************')


def demoDecor(fun):
    print('*'*(50))
    fun()
    print('*'*50)


@demoDecor
def message2():
    print("Python")

message2()

'''

# age can't be zero

def ageDecor(fun):
    def inner(a):
        if a < 0:
            print("Age can not be zero")
        else:
            return fun(a)
    return inner


@ageDecor
def age(x):
    print("Age is",x)

age(-13)