import pygame

from settings import Settings

class Ship:
    '''Klasa do zarządzania statkiem kosmicznym'''

    def __init__(self, ai_game):
        '''Inicjalizacja statku i jego połorzenia'''

        self.screen = ai_game.screen
        self.settings = Settings()

        #to store rectangular cordinates
        self.screen_rect = ai_game.screen.get_rect()

        #Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load(self.settings.ship_path_image)
        #resize
        self.image = pygame.transform.scale(self.image,(
            self.settings.ship_width,self.settings.ship_height))
        self.rect = self.image.get_rect()

        #nowy statek pojawia się na środku na dole
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Wyswietlenie w akualnym połozeniu'''

        self.screen.blit(self.image, self.rect)