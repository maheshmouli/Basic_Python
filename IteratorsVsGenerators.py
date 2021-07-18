#Generators vs Iterators

#Iterator
'''lst = [1,2,3,4]
iterable = iter(lst)
for i in iterable:
    print(i)

try:
    print(next(iterable))
    
except StopIteration:
    print("It is empty")'''

#Generators Here after adding yield it will make the entire
#function as generator
#yield will store the local variable value
#whatever generator is storing a iterator
#TO keep this simple, To create iterator we use iter() and to generator we use
#function along with yield keyword
#Generator uses the yield keyword, It saves the local variable
#Generator in python helps us to write fast and compact code
#Python iterator is much more memory efficient
#we use next keyword in iterators
def square(n):
    for i in range(n):
        yield i**2
square(3)
#for i in square(3):
#   print(i)
a = square(3)
print(next(a))

import types, collections
issubclass(types.GeneratorType, collections.Iterator)
