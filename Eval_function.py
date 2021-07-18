#Eval functin evaluates python expression which are written as strings
#How does eval work
# Parse python expression
# compile into a byte code
# evaluate the python expression
# it will return the result

#print(eval("5*5"))


#print(eval(input("Enter the python expression ")))


'''def square_num(num):
    return num**2

print(eval("square_num(2)"))'''

var = compile("5*5", '<string>', 'eval')
print(eval(var))


###Globals
x=10
print(eval("x+50+x**2", {'x': x}))

x = 100
z = 100
print(eval("x+z",{"x":x,"z":100}))


###Locals
print(eval("a+b+c",{},{"a":100,"b":200,"c":100}))

d=100
e=200
print(eval("d<e"))
