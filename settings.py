import pygame

class Settings:
    '''Aquí vamos a configurar los elementos necesarios para el juego'''

    def __init__(self) -> None:
        '''Definimos las características de la pantalla'''
        
        #Establecemos la velocidad de la nave
        self.ship_speed = 1.5


        #Establecemos las propiedades de la pantalla    
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)     #La pantalla completa podemos consultarla en la página 274


        # Establecemos la configuración de las balas
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        #Configuración del alien
        self.alien_speed = 0.4
        self.fleet_drop_speed = 5
        self.fleet_direction = 1

        