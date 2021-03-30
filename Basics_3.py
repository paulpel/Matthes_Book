#classes
print('\nClasses\n')

#first class
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

my_dog = Dog('Diora',8)
print(f'My dog\'s name is {my_dog.name.title()} and she is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()

you_dog = Dog("Max",2)
you_dog.sit()


class Car():
    '''Car info'''

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_full_name(self):
        '''Return full description of a car'''
        long_name = f'{self.brand} {self.model} {self.year}'
        return long_name.title()

my_car = Car('VW','golf 7',2016)
print(my_car.get_full_name())