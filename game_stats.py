class GameStats:
    '''Sigue las estadísticas de alien invasion'''

    def __init__(self, ai_game):
        '''Inicializa las estadísticas'''

        self.settings = ai_game.settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        '''Inicializa las estadísticas qe pueden cambiar durante el juego'''
        self.ships_left = self.settings.ship_limit