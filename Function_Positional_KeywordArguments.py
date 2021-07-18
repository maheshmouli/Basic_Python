#print functions
'''def even_odd(num):
    if num%2==0:
        print('Number is even')
    else:
        print('Number is odd')

num=24
even_odd(num)
'''

#return function
'''def hello_world():
    return 'Hello World'

val = hello_world()
print(val)
'''

#positional Arguments and Keyword Arguments
'''def hello(name, age):
    print('name: {} and age: {}'.format(name, age))

hello('Mouli', 23)'''


#args-positional arguments kwargs-keyword arguments
'''def hello(*args,**kwargs):
    print(args)
    print(kwargs)

#hello('Mouli','Mahesh',age=23,dob=1998) 
lst = ['Mouli','Mahesh']
dict_args = {'age':23, 'dob':1998}

hello(*lst, **dict_args)'''



#returning sum of even and odd numbers in a list using functions
def evenoddsum(lst):
    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
            even_sum = even_sum + i
        else:
            odd_sum = odd_sum + i

    return even_sum, odd_sum

lst=[8,4,1,3,99,13,21,22,46]
print(evenoddsum(lst))


            




