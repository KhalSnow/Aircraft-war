# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:15:26 2020

@author: Wyh
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    # Initialize bullet. 
    def __init__(self, setting, screen, rocket):
        super().__init__()
        self.screen = screen
        
        if rocket.heading_up:
            self.rect = pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
            self.rect.centerx = rocket.rect.centerx
            self.rect.top = rocket.rect.top
        elif rocket.heading_down:
            self.rect = pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
            self.rect.centerx = rocket.rect.centerx
            self.rect.top = rocket.rect.bottom
        
        self.bullet_y = float(self.rect.y)
        
        self.color = setting.bullet_color
        self.speed = setting.bullet_speed
    
    # Update bullet position. 
    def update(self, rocket):
        if rocket.heading_up:
            self.bullet_y -= self.speed
        elif rocket.heading_down:
            self.bullet_y += self.speed
        self.rect.y = self.bullet_y
    
    # Draw bullet. 
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)