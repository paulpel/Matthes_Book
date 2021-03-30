class Dog():
    '''Trying to model a dog'''

    def __init__(self, name, age):          #automatically will happen
        '''Initiation of name and age'''
        self.name = name        #self prefix to make it available to other methods in class
        self.age = age

    def sit(self):
        '''Simulation of a dog sitting'''
        print(f'{self.name.title()} now sits.')

    def roll_over(self):
        '''Simulation od a dog rolling over.'''
        print(f'{self.name.title()} now rolls.')

class Car():
    '''Car info'''

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_full_name(self):
        '''Return full description of a car'''
        long_name = f'{self.brand} {self.model} {self.year}'
        return long_name.title()

    def read_odometer(self):
        '''Display current kmeeters traveled'''
        print(f'{self.odometer_reading} km travelled so far.')

    def update_odometer(self, km_reading):
        '''Update info about odometer'''
        if km_reading >= self.odometer_reading:
            self.odometer_reading = km_reading
        else:
            print('Can\'t lower existing milleage!')

    def add_km_travelled(self, km):
        '''Add new travelled km to odometer'''
        self.odometer_reading += km

class ElectricCar(Car):
    '''Electric subclass of Car'''

    def __init__(self, brand, model, year):
        super().__init__(brand,model,year)
        self.battery_size = 75

    def describe_battery(self):
        print(f'Battery capacity is {self.battery_size} kWh')


my_dog = Dog('Diora',8)
print(f'My dog\'s name is {my_dog.name.title()} and she is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()
you_dog = Dog("Max",2)
you_dog.sit()

print('\n')

my_car = Car('VW','golf 7',2016)
print(my_car.get_full_name())
my_car.read_odometer()
my_car.update_odometer(23545)
my_car.read_odometer()
my_car.add_km_travelled(54)
my_car.read_odometer()
my_car.update_odometer(0)

print('\n')

my_tesla = ElectricCar('tesla','model s',2020)
print(my_tesla.get_full_name())
my_tesla.describe_battery()
#to overwrite existing method in subclass just use the same name
#can add classes to classes as atributes