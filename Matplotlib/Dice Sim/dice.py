from random import randint


class Dice():
    '''Class to represent single game dice'''

    def __init__(self, num_sides=6):
        '''Cube'''
        self.num_sides = num_sides

    def roll(self):
        '''Return values from 1 to num_sides (6 if dice is cubic)'''
        return randint(1, self.num_sides)
