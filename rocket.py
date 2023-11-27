# import pygame

# from settings import Settings

# class Rocket:
#     def __init__(self, rocky):
#         self.screen = rocky.screen
#         self.screen_rect = rocky.screen.get_rect()
#         self.settings = Settings()

#         self.image = pygame.image.load("images/shut.png")
#         self.rect = self.image.get_rect()

#         self.rect.center = self.screen_rect.center

#         self.moving_right = False
#         self.moving_left = False
#         self.moving_up = False
#         self.moving_down = False

#         self.x = float(self.rect.x)
#         self.y = float(self.rect.y)


#     def update(self):
#         if self.moving_right and self.rect.right < self.screen_rect.right:
#             self.x += self.settings.rocket_speed
#         if self.moving_left and self.rect.left > 0:
#             self.x -= self.settings.rocket_speed
#         if self.moving_up and self.rect.top > 0:
#             self.y -= self.settings.rocket_speed
#         if self.moving_down and  self.rect.bottom < self.screen_rect.bottom:
#             self.y += self.settings.rocket_speed

#         self.rect.x = self.x
#         self.rect.y = self.y
            


#     def blit_space(self):
#         self.screen.blit(self.image, self.rect)

import pygame
from settings import Settings

class Shuttle:
    def __init__(self, shutty):
        self.screen = shutty.screen
        self.screen_rect = shutty.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.image.load("images/shut.png")
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        
        self.rect.centery = self.screen_rect.centery
        

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.double_speed = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.shuttle_speed
            if self.double_speed:
                self.x += self.settings.shuttle_double_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.shuttle_speed
            if self.double_speed:
                self.x -= self.settings.shuttle_double_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.shuttle_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.shuttle_speed
        
        self.rect.x = self.x
        self.rect.y = self.y

    def blit_shuttle(self):
        self.screen.blit(self.image, self.rect)

    def center_shuttle(self):
        self.rect.centery = self.screen_rect.centery
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

