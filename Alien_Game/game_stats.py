class GameStats:
    '''Monitorowanie statystyki gry'''

    def __init__(self, ai_game):
        '''Inicjalizacja danych statystycznych'''
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        '''Dane zmieniające się w trakcie gry'''
        self.ships_left = self.settings.ship_limit