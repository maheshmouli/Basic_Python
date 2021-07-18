#In Exception Handling, we need to write the child class above and later the
#generic class or exception
'''try:
    ##code block where exception can occur
    a=b
except NameError:
    print('Variable is not defined')
except Exception as e:
    print(e)'''

'''try:
    ##code block where exception can occur
    a=1
    b='e'
    c=a+b
except NameError:
    print('Variable is not defined')
except TypeError:
    print('Both datatypes shoulld be similar')
except Exception as e:
    print(e)'''

#Basic Exception Handling
'''try:
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    c = a/b
    d = a*b
    e = a+b
    print(c)
    print(d)
    print(e)
except NameError:
    print('Variable is not defined')
except ZeroDivisionError:
    print('Zero is not divisable with numbers')
except TypeError:
    print('Both datatypes shoulld be similar')
except Exception as e:
    print(e)'''


## We can also use try else
'''try:
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    c = a/b
    d = a*b
    e = a+b
    
except NameError:
    print('Variable is not defined')
except ZeroDivisionError:
    print('Zero is not divisable with numbers')
except TypeError:
    print('Both datatypes shoulld be similar')
except Exception as e:
    print(e)
else:
    print(c)
    print(d)
    print(e)'''



##We can use finally clause as well.
try:
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    c = a/b
    
except NameError:
    print('Variable is not defined')
except ZeroDivisionError:
    print('Zero is not divisable with numbers')
except TypeError:
    print('Both datatypes shoulld be similar')
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print('Execution is done')
