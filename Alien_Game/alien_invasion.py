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


            #Odświeżenie ekranu
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #Wyświetl ostatnio zmodyfikowany ekran
            pygame.display.flip()

    def _check_events(self):
        '''Reakcja na zdarzenia generowane przez klawiaturę i mysz'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    #Utworzenie egzemplarza i uruchomienie
    ai = AlienInvasion()
    ai.run_game()