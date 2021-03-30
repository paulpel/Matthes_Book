import sys

import pygame

class AlienInvasion:
    '''Klasa stworzona do zarządzania zasobami i sposobem działania gry'''

    def __init__(self):
        '''Inicjalizacja gry i utworzenie jej zasobów'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien invasion")

        #Zmiana koloru tła
        self.bg_color = (255,204,204)

    def run_game(self):
        '''Główna pętla gry - rozpoczęcie'''
        while True:
            #Oczekiwanie na nacisniecie klawisza badz przycisku myszy
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Odświeżenie ekranu
            self.screen.fill(self.bg_color)

            #Wyświetl ostatnio zmodyfikowany ekran
            pygame.display.flip()

if __name__ == '__main__':
    #Utworzenie egzemplarza i uruchomienie
    ai = AlienInvasion()
    ai.run_game()