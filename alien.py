import pygame 
from pygame.sprite import Sprite
from paths import Paths

class Alien(Sprite):
    '''Para representar un solo alien'''

    def __init__(self, ai_game):
        '''Inicializa el alien y lo pone en su posicion inicial'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Cargamos la imagen del alien y configuramos su atributo rect
        self.path = Paths('resources\\alien.png').__str__()
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect()

        # Posicionamos al alien el la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Guardamos la posicion horizontal exacta del alien
        self.x = float(self.rect.x)



    def check_edges(self):
        '''Devuelve True si el alien está en el borde de la pantalla'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True
        

    
    def update(self):
        '''Mueve la nave hacia la derecha'''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x


 