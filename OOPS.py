#OOPS in Python
class Car:
    def __init__(self, window, door, enginetype):
        self.windows = window
        self.doors = door
        self.enginetype=enginetype

    def self_driving(self):
        return "This is a {} car".format(self.enginetype)


car1 = Car(4,5,'Petrol')
print(car1.self_driving())
car2 = Car(3,4,'Diesel')

print(car1.windows)
print(car2.windows)


#Always creating should have fixed parameters, or else it will allow to create
#any number of objects and parameters

