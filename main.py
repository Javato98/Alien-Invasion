import pygame
from settings import Settings 
from ship import Ship
from alien import Alien
from bullet import Bullet
import sys



class AlienInvansion:
    '''Clase general para gestionar el juego y los recursos de este'''
    
    def __init__(self) -> None:
        '''Inicializa el juego y  crea recursos'''

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Metemos el propio juego como parametro
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.create_fleet()

 
    def run_game(self):
        '''Inicia el bucle principal para el juego'''

        while True:
            self._check_events()
            self.ship.update()
            self.update_bullets()
            self.update_aliens()
            self._update_screen()
            


    def _check_keydown_events(self, event):
        '''Responde a las pulsaciones de las teclas'''

        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_SPACE:
            self.fire_bullet()
        
        elif event.key == pygame.K_q:
            sys.exit()



    def _check_keyup_events(self, event):
        '''Responde a  las liberaciones de las teclas'''

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    
    def fire_bullet(self):
        '''Crea una bala nueva y la añade al grupo de balas'''

        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            print(len(self.bullets))

    
    def create_fleet(self):
        '''Creamos la flota de alienígenas'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Calculamos los aliens que caben en horizontal
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Calculamos las filas de aliens que caben en la pantalla
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)


    def create_alien(self, alien_number, row_number):
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien_height + 2 * alien_height * row_number
            self.aliens.add(alien)




    def update_bullets(self):
        '''Actualiza la posición de las balas y se deshace de las viejas'''

        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def update_aliens(self):
        '''Comprueba si la flota está en un brode, después actualiza las posiciones de todos los aliens de la flota'''
        self._check_fleet_edges()
        self.aliens.update()


    def _check_fleet_edges(self):
        '''Responde en el caso de que algún alien haya llegado al borde'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()

    
    def _change_fleet_direction(self):
        '''Baja toda la flota y cambia su dirección'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _check_events(self):
        '''Busca eventos de teclado y raton'''
        
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)



    def _update_screen(self):
        '''Actualiza a pantalla'''

        # Configura el color del fondo
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        #Hacer visible la última pantalla dibujada
        pygame.display.flip()


         

# ALGORITMO PRINCIPAL

if __name__ == '__main__':
    #Hace una instacia del juego y o ejecuta
    ai = AlienInvansion()
    ai.run_game()