#Filter functions
#It is used to return the conditional satisfied elements.

'''def even(num):
    if num%2==0:
        return True

lst = [2,4,5,6,7,8,9,11]
print(list(filter(even, lst)))'''


#we can even pass lambda funtion as parameters

lst = [2,4,5,6,7,8,9,11]
print(list(filter(lambda num:num%2==0, lst)))


#In map function we get each and every element, but in filter it gives only the
#true elements



