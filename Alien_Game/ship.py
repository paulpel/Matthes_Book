import pygame

class Ship:
    '''Klasa do zarządzania statkiem kosmicznym'''

    def __init__(self, ai_game):
        '''Inicjalizacja statku i jego połorzenia'''

        self.screen = ai_game.screen
        self.settings = ai_game.settings

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

        #położenie poziome musimy dac zmiennoprzecinkowe - zeby zmienic predkosc
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Czy statek się porusza
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Uaktualnienie położenia statku'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        '''Wyswietlenie w akualnym połozeniu'''

        self.screen.blit(self.image, self.rect)