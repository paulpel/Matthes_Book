import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Klasa stworzona do zarządzania zasobami i sposobem działania gry'''

    def __init__(self):
        '''Inicjalizacja gry i utworzenie jej zasobów'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)

    def run_game(self):
        '''Główna pętla gry - rozpoczęcie'''
        while True:
            #Oczekiwanie na nacisniecie klawisza badz przycisku myszy
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        '''Reakcja na zdarzenia generowane przez klawiaturę i mysz'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #przesuniecie w prawo
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    #przesuniecie w prawo
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    #przesuniecie w prawo
                    self.ship.moving_left = False


    def _update_screen(self):
        '''Uaktualnienie ekranu'''
        # Odświeżenie ekranu
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Wyświetl ostatnio zmodyfikowany ekran
        pygame.display.flip()

if __name__ == '__main__':
    #Utworzenie egzemplarza i uruchomienie
    ai = AlienInvasion()
    ai.run_game()