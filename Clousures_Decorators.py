#Closures and Decorators

#Closures
'''def main_welcome():
    msg = "Hello"
    def sub_welcome():
        print('Welcome')
        print(msg)
        print('How are u?')
    return sub_welcome()

print(main_welcome())'''

#Decorators
def main_welcome(func):
    
    def sub_welcome():
        print('Welcome')
        func()
        print('How are u?')
    return sub_welcome()

@main_welcome
def channel_name():
    print('This is Mouli')
print(main_welcome(channel_name()))

