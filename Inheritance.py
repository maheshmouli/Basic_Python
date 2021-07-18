class Car():
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype
    def drive(self):
        print('The person drive the car')

class audi(Car):
    def __init__(self, windows, doors, enginetype, enableai):
        super().__init__(windows, doors, enginetype)
        self.enableai = enableai
    def selfdriving(self):
        print('Audi supports self driving')

audiQ7 = audi(6,4,'Diesel',True)
print(audiQ7.drive())
