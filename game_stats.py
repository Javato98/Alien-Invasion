class GameStats:
    '''Sigue las estadísticas de alien invasion'''

    def __init__(self, ai_game):
        '''Inicializa las estadísticas'''
        self.settings = ai_game.settings
        self.game_active = False
        self.high_score = 0
        self.ships_left = self.settings.ship_limit
        self.reset_stats()

    def reset_stats(self):
        '''Inicializa las estadísticas qe pueden cambiar durante el juego'''
        self.score = 0 
        self.level = 0
        