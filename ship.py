import pygame
from paths import Paths
from pygame.sprite import Sprite



class Ship(Sprite):
    '''Creamos la clase nave'''

    def __init__(self, ai_game) -> None:
        '''Inicializa la nave y confura su posicion inicial'''


        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.path = Paths('resources\\ships\\alienspaceship.png').__str__()

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect()

        # Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla 
        self.rect.midbottom = self.screen_rect.midbottom

        # Bandera (condición booleana) de movimiento
        self.moving_right = False
        self.moving_left = False

        #Instanciamos los ajustes de que hemos desarrollado para el juego
        self.settings = ai_game.settings
        
        #Guardamos un valor decimal para la posicion de la nave
        self.x = float(self.rect.x)


    def update(self):
        '''Actualizamos el movimiento'''

        #Actualiza el valor de la nave y no el rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed 

        #Actualizamos el valor de la nave
        self.rect.x = self.x


    def center_ship(self):
        '''Centramos la nave en la pantalla'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

            

    def blitme(self):
        '''Dibuja la nave en su ubicación actual'''

        self.screen.blit(self.image, self.rect)


