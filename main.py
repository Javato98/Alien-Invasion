import pygame
from settings import Settings 
from ship import Ship
from alien import Alien
from bullet import Bullet
import sys
from time import sleep
from game_stats import GameStats
from button import Button



class AlienInvansion:
    '''Clase general para gestionar el juego y los recursos de este'''
    
    def __init__(self) -> None:
        '''Inicializa el juego y  crea recursos'''

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Creamos una instancia para guardar las estadísticas del juego
        self.stats = GameStats(self)

        # Metemos el propio juego como parametro
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.play_button = Button(self, "Play")

        self._create_fleet()

 
    def run_game(self):
        '''Inicia el bucle principal para el juego'''

        while True:
            self._check_events()

            if self.stats.game_active:
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



    def _create_fleet(self):
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

        self._check_bullet_alien_collision()



    def _check_bullet_alien_collision(self):
        '''Responde a las colisiones de bala-alien'''

        # Retira las balas y los aliens que han chocado
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destruuye las balas existentes y crea una flota nueva
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    

    def update_aliens(self):
        '''Comprueba si la flota está en un borde, después actualiza las posiciones de todos los aliens de la flota'''
        self._check_fleet_edges()
        self.aliens.update()

        # Busca colisiones alien - nave
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()


    def _ship_hit(self):
        '''Responde al impacto de un alien con la nave'''

        if self.stats.ships_left > 0:
            # Disminuye ship_left
            self.stats.ships_left -= 1

            # Se deshace de las naves y las balas restantes
            self.aliens.empty()
            self.bullets.empty()

            # Crea una flota nueva y centra la nave 
            self._create_fleet()
            self.ship.center_ship()

            # Pausa
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        '''Comprobamos que los aliens llegan al fondo de la pantalla'''
        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break




    def _check_fleet_edges(self):
        '''Responde en el caso de que algún alien haya llegado al borde'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(self.mouse_pos)

    
    def _check_play_button(self, mouse_pos):
        '''Comprueba si se ha clickado en el botón, y lo inicia si es True'''
        buttom_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if buttom_clicked and not self.stats.game_active:
            # Restablece las estadísticas del juego
            self.stats.reset_stats()
            self.stats.game_active = True 

            # Se deshace de los aliens y de las balas
            self.aliens.empty()
            self.bullets.empty()

            # Crea una nueva flota y centra la nave
            self._create_fleet()
            self.ship.center_ship()
            self.settings.inicializate_dynamic_settings()

            # Oculta el cursor del ratón
            pygame.mouse.set_visible(False)





    def _update_screen(self):
        '''Actualiza a pantalla'''

        # Configura el color del fondo
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()

        #Hacer visible la última pantalla dibujada
        pygame.display.flip()


         

# ALGORITMO PRINCIPAL

if __name__ == '__main__':
    #Hace una instacia del juego y o ejecuta
    ai = AlienInvansion()
    ai.run_game()