#for future updation of a value in class variable it is better to use
#class method. This will help auto updation of old class variable as well.

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


Car.revise_base_price(0.10)
print(Car.base_price)

car1 = Car(4,5,2000)
print(car1.base_price)
            
