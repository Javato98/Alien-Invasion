import pygame.font

class Button():

    def __init__(self, ai_game, msg):
        '''Inicializa los atributos del botón'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # EConfigura las dimensiones y propiedades del botón
        self.width, self.height = 30, 100
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Creamos el objeto rect botón y lo centramos 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Preparamos el mensaje del botón
        self._prep_msg(msg)





        