class Settings:
    '''Klasa do przechowywania ustawień'''

    def __init__(self):
        '''Inicjalizacja ustawień gry'''
        #Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,204,204)

        #Ustawienia statku
        self.ship_width = 37
        self.ship_height = 64
        self.ship_path_image = 'Images/ship.bmp'