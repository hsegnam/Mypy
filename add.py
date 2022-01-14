# Function is collection of block od statements organized under a single named unit
# Functions reduces the code rewriting as same code can be wriiten once and used again and again
'''
	def keyword is used to define a function
	function can have none or many arguments or parameters
	to use the funcion we must call it with its name

Syntax of Function
	def fun_name(arguments/parameter list,):
		block of statements

'''

def addition():
	a = int(input('Enter a number'))
	b = int(input('Enter a number'))
	c = a+b
	print("Addition = ",c)

addition()
