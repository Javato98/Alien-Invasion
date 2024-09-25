import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):
    '''En esta clase vamos a gestionar las balas que dispara la nave'''


    def __init__(self, ai_game):
        '''Crea un objeto para gestionar las balas disparadas desde a nave'''

        super().__init__()

        #Estableciendo las configuraciones para las balas
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Establecemos el rectángulo de la bala 
        self.rect = pygame.Rect( (0,0), (self.settings.bullet_width, self.settings.bullet_height))
        self.rect.midtop = ai_game.ship.rect.midtop # Movemos la bala a la ubicación correcta

        self.y = float(self.rect.y)

    
    def update(self):
        '''Mueve la bala hacia arriba por la pantalla'''

        # Movemos la bala hacia arriba
        self.y -= self.settings.bullet_speed
        
        # Actualizamos la posición del rectángulo
        self.rect.y = self.y


    def draw_bullet(self):
        '''Dibujamos las balas en la pantalla'''

        pygame.draw.rect(self.screen, self.color, self.rect)

        