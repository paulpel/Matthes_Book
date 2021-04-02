import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Klasa przedstawiająca obcego'''

    def __init__(self, ai_game):
        '''Inicjalizacja zmiennych i położenia'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect
        self.image = pygame.image.load(self.settings.alien_image_path)
        self.image = pygame.transform.scale(self.image, (
            self.settings.alien_width, self.settings.alien_height))
        self.rect = self.image.get_rect()

        #Umieszczenie nowego obcego w lewym rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)