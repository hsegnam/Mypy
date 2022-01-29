'''
In python a function can return more than one value

'''

def add(a,b):
    c = a+b
    return c
def message():
    return "This is returned message"

res = add(2,4)
print(type(res))
print(res)
print(type(message()))
print(message())

def add1(a,b):
    c = a+b
    return a,b,c
x = add1(5,6)
print(type(x))
print(x)

