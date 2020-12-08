# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:05:38 2020

@author: Wyh
"""

import pygame
from pygame.sprite import Sprite

# A class to define rocket. 
class Rocket(Sprite):
    
    # Initialize rocket and its position. 
    def __init__(self, setting, screen):
        super().__init__()
        self.screen = screen
        self.setting = setting
        
        # Heading up. 
        self.heading_up = True
        self.heading_down = False
        
        # Load the rocket image, and get its rect. 
        self.image_up = pygame.image.load('rocket_up.bmp')
        self.image_down = pygame.image.load('rocket_down.bmp')
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Put the rocket at the mid bottom of screen. 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery
        
        # Store decimal. 
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.rocket_y = float(self.rect.y)
        
        # Moving sign. 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update_rocket(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.setting.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.setting.rocket_speed
        if self.moving_up and self.heading_up and self.rect.y > 0:
            self.rocket_y -= self.setting.rocket_speed
            self.rect.y = self.rocket_y
        if self.moving_down and self.heading_down and self.rect.y < self.screen_rect.bottom-self.rect.height:
            self.rocket_y += self.setting.rocket_speed
            self.rect.y = self.rocket_y
        self.rect.centerx = self.center_x

    # Get image. 
    def get_image(self):
        if self.heading_up:
            self.image = self.image_up
        elif self.heading_down:
            self.image = self.image_down
        return self.image

    # Draw the rocket at certain position. 
    def blit(self):
        if self.heading_up:
            self.image = self.image_up
            self.screen.blit(self.image, self.rect)
        elif self.heading_down:
            self.image = self.image_down
            self.screen.blit(self.image, self.rect)
        
    # Center rocket. 
    def center_rocket(self):
        self.center_x = self.screen_rect.centerx
        self.rocket_y = self.screen_rect.centery-self.rect.height
        # self.rocket_y = self.screen_rect.bottom-self.rect.height
        self.rect.y = self.rocket_y