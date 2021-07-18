#also known as anonymous function (a function with no name)
'''add = lambda a,b:a+b
print(add(12,14))

even = lambda a:a%2==0
print(even(24))


addition = lambda x,y,z:x+y+z
print(addition(1,2,4))

#Factorial of a number

fact = lambda x: x*fact(x-1) if (x>=1) else 1
print(fact(1))'''

#Can also used to return the lambda function
import math

def myfunc(n):
    return lambda x:math.pow(x,n)

squ = myfunc(2)
cube = myfunc(3)
squareroot = myfunc(0.5)

print(squ(3))
print(cube(3))
print(squareroot(3))

