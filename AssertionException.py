#Assertion Exception
'''Python provides the assert statement to check if a given logical expression
is true or false. Program execution proceeds only if the expression is true and
raises the AssertionError when it is false.'''

num = 10
assert num>=10

try:
    n = int(input('enter a number: '))
    assert n%2==0
    print('The number is even')
except AssertionError:
    print('entered number is odd')
