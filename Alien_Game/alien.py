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

    def update(self):
        '''Przesuniecie w prawo'''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x =self.x

    def check_edges(self):
        '''Zwraca True jezeli obcy jest przy krawwedzi'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >=screen_rect.right or self.rect.left <= 0:
            return True

