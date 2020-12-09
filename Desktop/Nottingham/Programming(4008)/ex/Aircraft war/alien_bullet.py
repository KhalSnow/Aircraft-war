# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 00:34:07 2020

@author: Wyh
"""

import pygame
from pygame.sprite import Sprite

class Alien_Bullet(Sprite):
    
    # Initialize alien bullet. 
    def __init__(self, setting, screen, alien, alien_bullets):
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0,0,setting.alien_bullet_width,setting.alien_bullet_height)
        
        if alien.rect.y < setting.screen_height / 2:
            self.rect.centerx = alien.rect.centerx
            self.rect.bottom = alien.rect.bottom
        else:
            self.rect.centerx = alien.rect.centerx
            self.rect.bottom = alien.rect.top
        
        self.alien_bullet_y = float(self.rect.y)
        
        self.color = setting.alien_bullet_color
        self.speed = setting.alien_bullet_speed
    
    # Update alien bullet position. 
    def update(self, setting):
        if self.alien_bullet_y <= setting.screen_height / 2:
            self.alien_bullet_y += self.speed
        else:
            self.alien_bullet_y -= self.speed
        self.rect.y = self.alien_bullet_y
    
    # Draw bullet. 
    def draw_alien_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)