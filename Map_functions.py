def even_odd(num):
    if num%2==0:
        return True
    else:
        return False

lst = [1,4,2,5,7,8,9,10,22,14,15,24,16,88,68]
print(list(map(even_odd, lst)))
