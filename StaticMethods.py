#In Static Method, we don't need to provide the class parameter or the
#instance parameter(self). Whenever the class loads staticmethod get initialized
#first. We cannot create multiple copies of static methods.


import datetime
now = datetime.datetime.now()

class Car:
    base_price = 1000000
    def __init__(self, windows, doors, power):
        self.windows = windows
        self.doors = doors
        self.power = power

    def car_base_price(self):#it is refering to this particular class instance
        print('The base price is {}'.format(self.base_price))
    @classmethod
    def revise_base_price(cls, inflation):
        cls.base_price = cls.base_price+cls.base_price*inflation

    @staticmethod
    def check_year():
        if now.year==2021:
            return True
        else:
            return False

car1 = Car(4,5,2000)
if (car1.check_year()):
    pass
else:
    Car.revise_base_price()
print(car1.base_price)
