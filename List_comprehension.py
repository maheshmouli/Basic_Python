#List comprehensions provide a concise way to create lists.
#It consist of brackets containing an expression followed by a far clause, then
#zero or more for or if clauses.

'''lst1 = []
def lst_squ(lst):
    for i in lst:
        lst1.append(i*i)
    return lst1

print(lst_squ([1,2,3,4,5,6]))'''

#the above can be written in single line using List Comprehension

lst = [1,2,3,4,5,6]
lst1 = [i*i for i in lst if i%2==0]
print(lst1)
