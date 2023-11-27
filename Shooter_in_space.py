# import pygame

# import sys

# from rocket import Rocket
# from settings import Settings

# class Spacerocket:
#     def __init__(self):
#         pygame.init()
#         self.settings = Settings()
#         self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
#         self.rocket = Rocket(self)
#         pygame.display.set_caption("Rocket")

#     def run_game(self):
#         while True:
#             self.check_events()
#             self.rocket.update()
#             self.update_screen()


#     def check_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 self.check_keydown_events(event)
#             if event.type == pygame.KEYUP:
#                 self.check_keyup_events(event)
            

#     def check_keydown_events(self, event):
#         if event.key == pygame.K_RIGHT:
#             self.rocket.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.rocket.moving_left = True
#         elif event.key == pygame.K_UP:
#             self.rocket.moving_up = True
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = True

#     def check_keyup_events(self, event):
#         if event.key == pygame.K_RIGHT:
#             self.rocket.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.rocket.moving_left = False
#         elif event.key == pygame.K_UP:
#             self.rocket.moving_up = False
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = False

#     def update_screen(self):
#         self.screen.fill(self.settings.bg_color)
#         self.rocket.blit_space()
#         pygame.display.flip()

# if __name__ == "__main__":
#     ris = Spacerocket()
#     ris.run_game()



    





import pygame
import sys
from time import sleep

from rocket import Shuttle
from settings import Settings
from bullets import Bullets
from alien import Alien
from game_stats import Game_Stats
from button import Button
from rectangle import Rectangle

class Shuttle_in_space:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.stats = Game_Stats(self)
        pygame.display.set_caption("Hello!")
        self.shuttle = Shuttle(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_aliens()
        self.play_button = Button(self, "Play")
        self.rectangle = Rectangle(self)


    def run_game(self): 
        while True:
            self.check_events()
            if self.stats.game_active:
                self.shuttle.update()
                self._update_bullets()
                self._update_aliens()
                self.update_rectangle()
            self._update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.shuttle.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.shuttle.moving_left = True
        elif event.key == pygame.K_UP:
            self.shuttle.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.shuttle.moving_down = True
        elif event.key == pygame.K_LSHIFT:
            self.shuttle.double_speed = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_p:
            self._start_game()
        

    def _check_play_button(self, mouse_pos):
        button_cliked =  self.play_button.rect.collidepoint(mouse_pos)
        if button_cliked and not self.stats.game_active:
            self._start_game()

            self.aliens.empty()
            self.bullets.empty()

            self._create_aliens()
            self.shuttle.center_shuttle()
            # pygame.mouse.set_visible(False)
        
    def _start_game(self):
        self.stats.reset_ship()
        self.stats.game_active = True

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.shuttle.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.shuttle.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.shuttle.moving_down = False
        elif event.key == pygame.K_UP:
            self.shuttle.moving_up = False
        elif event.key == pygame.K_LSHIFT:
            self.shuttle.double_speed = False
    
    def _fire_bullets(self):
        new_bullet = Bullets(self)
        self.bullets.add(new_bullet)
    
    def _update_bullets(self):
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.left >= self.shuttle.screen_rect.right:
                    self.bullets.remove(bullet)
                # print(len(self.bullets))
            self.check_bullet_alien_collision()
        
    def check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens,  True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_aliens()
            self.shuttle.center_shuttle()
    
    def _update_aliens(self):
        self._check_aliens_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.shuttle, self.aliens):
            self._ship_hit()
        self._check_aliens_at_edge()
    
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self._create_aliens()
            self.shuttle.center_shuttle()
            
            sleep(0.5)
        else:
            self.stats.game_active = False
            # pygame.mouse.set_visible(True)
    
    def _check_aliens_at_edge(self):
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                self._ship_hit()
                break

    def _create_aliens(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        shuttle_width = self.shuttle.rect.width
        available_space_x = self.settings.screen_width - (3 * alien_width) - shuttle_width
        rows_number = available_space_x // (2 * alien_width)
        available_space_y = self.settings.screen_height - (2 * alien_height)
        aliens_number = available_space_y // (2 * alien_height)
        for row_number in range(rows_number):
            for alien_number in range(aliens_number):
                self._create_alien(alien_number, row_number)
        
    def _create_alien(self, al_n, row_n):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = self.settings.screen_width - alien_width - 2 * alien_width * row_n
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * al_n
        alien.rect.y = alien.y
        self.aliens.add(alien)
        
    def _check_aliens_edges(self): 
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_aliens_direction()
                break
    

    def _change_aliens_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.drop_speed
        self.settings.aliens_direction *= -1

    def update_rectangle(self):
        self._check_rects_edges()
        self.rectangle.update()

    # def _check_rects_edges(self):
    #     if self.rectangle.rect.top <= 0 or self.rectangle.rect.bottom >= self.settings.screen_height:
    #         self.rectangle.rect.x -= self.settings.rects_drop_speed
    #         self.settings.rects_direction *= -1
    
    # def _check_rects_edges(self):
    #     if self.rectangle._check_edges():
    #         self.rectangle.rect.x -= self.settings.rects_drop_speed
    #         self.settings.rects_direction *= -1
    
    def _check_rects_edges(self):
            # if self.rectangle.rect.y == 0 or self.rectangle.rect.y == self.settings.screen_height:
            if self.rectangle._check_edges():
                self._change_rects_direction()
            

        # self.rectangle.update()
        # else:
            # self.rectangle.update()

    
    def _change_rects_direction(self):
                self.rectangle.rect.x -= self.settings.rects_drop_speed
                self.settings.rects_direction *= -1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.shuttle.blit_shuttle()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()
        self.rectangle.draw_rectangle()
        pygame.display.flip()

if __name__ == "__main__":
    shut = Shuttle_in_space()
    shut.run_game()       

    


