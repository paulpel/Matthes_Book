class Settings:
    '''Klasa do przechowywania ustawień'''

    def __init__(self):
        '''Inicjalizacja ustawień gry'''
        #Ustawienia ekranu
        self.screen_width = 2560
        self.screen_height = 1600
        self.bg_color = (255,204,204)
        self.bg_image_path = 'Images/galaxy_bg.bmp'

        #Ustawienia statku
        self.ship_width = 37
        self.ship_height = 64
        self.ship_path_image = 'Images/ship.bmp'
        self.ship_speed = 2

        #Ustawienia pocisku
        self.bullet_speed = 2.5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255,0,0)