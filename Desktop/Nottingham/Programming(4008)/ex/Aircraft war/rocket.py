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
        
        # Load the rocket image, and get its rect.
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Put the rocket at the mid bottom of screen. 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store decimal. 
        self.center = float(self.rect.centerx)
        self.rocket_y = float(self.rect.y)
        
        # Moving sign. 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update_rocket(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.setting.rocket_speed
        if self.moving_up and self.rect.y > 0:
            self.rocket_y -= self.setting.rocket_speed
            self.rect.y = self.rocket_y
        if self.moving_down and self.rect.y < self.screen_rect.bottom-self.rect.height:
            self.rocket_y += self.setting.rocket_speed
            self.rect.y = self.rocket_y
        self.rect.centerx = self.center

    # Draw the rocket at certain position. 
    def blit(self):
        self.screen.blit(self.image, self.rect)
        
    # Center rocket. 
    def center_rocket(self):
        self.center = self.screen_rect.centerx
        self.rocket_y = self.screen_rect.bottom-self.rect.height
        self.rect.y = self.rocket_y