import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Klasa do zarządzania pociskami'''

    def __init__(self,ai_game):
        '''Utworzenie pocisku w aktualnym położeniu statku'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #utworzenie pocisku w 0,0 i odpowiednie ułożenie
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        '''Poruszanie sie pocisków'''
        #uaktualnienie położenia pocisku
        self.y -= self.settings.bullet_speed
        #uaktualnienie położenia prostokąta pocisku
        self.rect.y = self.y

    def draw_bullet(self):
        '''Wyświetlanie pocisku na ekranie'''
        pygame.draw.rect(self.screen, self.color, self.rect)