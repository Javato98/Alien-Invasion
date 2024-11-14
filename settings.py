import pygame

class Settings:
    '''Aquí vamos a configurar los elementos necesarios para el juego'''

    def __init__(self) -> None:
        '''Definimos las características de la pantalla'''
        
        #Establecemos las vidas que tenemos en el juago
        self.ship_limit = 3


        #Establecemos las propiedades de la pantalla    
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)     #La pantalla completa podemos consultarla en la página 274


        # Establecemos la configuración de las balas
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        #Configuración del alien
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        
        # Rapidez con la que acelera el juego
        self.speedup_scale = 1.1

        self.score_scale = 1.2

        self.inicializate_dynamic_settings()

    def inicializate_dynamic_settings(self):
        '''Inicializa las configuraciones que van cambiando durante el juego'''
        self.ship_speed = 0.6
        self.bullet_speed = 1
        self.alien_speed = 0.3

        self.fleet_direction = 1

        #Puntuación
        self.alien_points = 50


    def increase_speed(self):
        '''Incrementa las configuraciones de velocidad'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


        