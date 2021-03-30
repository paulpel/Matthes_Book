import sys

import pygame

from settings import Settings

class AlienInvasion:
    '''Klasa stworzona do zarządzania zasobami i sposobem działania gry'''

    def __init__(self):
        '''Inicjalizacja gry i utworzenie jej zasobów'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        '''Główna pętla gry - rozpoczęcie'''
        while True:
            #Oczekiwanie na nacisniecie klawisza badz przycisku myszy
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Odświeżenie ekranu
            self.screen.fill(self.settings.bg_color)

            #Wyświetl ostatnio zmodyfikowany ekran
            pygame.display.flip()

if __name__ == '__main__':
    #Utworzenie egzemplarza i uruchomienie
    ai = AlienInvasion()
    ai.run_game()