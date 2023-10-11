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

from rocket import Shuttle
from settings import Settings
from bullets import Bullets

class Empty:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.shuttle = Shuttle(self)
        pygame.display.set_caption("Hello!")
        self.bullets = pygame.sprite.Group()

    def run_game(self): 
        while True:
            self.check_events()
            self.shuttle.update()
            self.update_bullets()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self.check_keyup_events(event)

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
        # print(event.key)
    
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
    
    def update_bullets(self):
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.left >= self.shuttle.screen_rect.right:
                    self.bullets.remove(bullet)
                print(len(self.bullets))


        
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.shuttle.blit_shuttle()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == "__main__":
    shut = Empty()
    shut.run_game()       

    


