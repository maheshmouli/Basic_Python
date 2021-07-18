#Custom Exceptions(Jupyter)

class Error(Exception):
    pass

class dobException(Error):
    pass


year = int(input('Date of Birth: '))
age = 2021 - year
try:
    if age<=30 & age>20:
        print("You are valid to play this game")
    else:
        raise dobException
except dobException:
    print("Below 18 years are not allowed to play this game")
    
