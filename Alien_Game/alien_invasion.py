import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''Klasa stworzona do zarządzania zasobami i sposobem działania gry'''

    def __init__(self):
        '''Inicjalizacja gry i utworzenie jej zasobów'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_image = pygame.image.load(self.settings.bg_image_path).convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")
        pygame.mouse.set_visible(False)

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        '''Główna pętla gry - rozpoczęcie'''
        while True:
            #Oczekiwanie na nacisniecie klawisza badz przycisku myszy
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        '''Reakcja na zdarzenia generowane przez klawiaturę i mysz'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        #reakcja na nacisniecie klawisz
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        #reakcja na zwolnienie klawisz
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        '''Stworzenie pocisku i dodanie go do grupe pocisków'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''Aktualizacja pocisków i usuwanie tych spoza ekranu'''
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_collision()


    def _check_bullet_collision(self):
        '''Usuniecie pociskow i obcych oraz stworzenie nowej floty'''
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()


    def _create_alien(self, alien_number, row_number):
        '''Utworzenie obcego i umieszczenie go w rzedzie'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2.5 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        '''Utworzenie floty'''
        #Utworzenie obcego
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (3*alien_width)
        number_aliens_x = available_space_x//(2*alien_width)

        #ile rzędów
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (5*alien_height)-ship_height)
        number_of_rows = available_space_y//(2*alien_height) - 1

        #Flota obcych
        for row_number in range(number_of_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        '''Reakcja na dotarcie do krawedzi'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Przesuniecie floty w doł i zmiana kierunku w którym się porusza'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        '''Reakcja na trafienie w statek'''
        self.stats.ships_left -= 1

        #reset aliens i bullets
        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        sleep(0.5)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        #wykrywanie kolizji między obcym i statkiem
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _update_screen(self):
        '''Uaktualnienie ekranu'''
        # Odświeżenie ekranu
        self.screen.blit(self.bg_image, (0,0))
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


        # Wyświetl ostatnio zmodyfikowany ekran
        pygame.display.flip()

if __name__ == '__main__':
    #Utworzenie egzemplarza i uruchomienie
    ai = AlienInvasion()
    ai.run_game()