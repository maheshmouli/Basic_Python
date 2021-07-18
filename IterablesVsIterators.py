#Python list Iterables vs Iterators
#In iterable memory is initialized first but in iterators memory will not
#initialized first one by one it will give memory.

#List Iterable
lst = [1,2,3,4,5,6,7,8]

#for i in lst:
#    print(i)

#list Iterator-used to call when we use only e.g:next(lst1)
lst1 = iter(lst)
for i in lst1:
    print(i)

