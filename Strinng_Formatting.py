#String Formatting
'''def greetings(name):
    return "Hello {}. Welcome to the community".format(name)

print(greetings('Mahesh'))'''


'''def welcome(name, age):
    return "My name is {}. My age is {}".format(name, age)

print(welcome("Mahesh", 23))'''

#We are passing the values in the form of dictionary
a_dict = {'name':'Mahesh','age': 23}

print("My name is {name} and I'm {age} years old".format(**a_dict))
