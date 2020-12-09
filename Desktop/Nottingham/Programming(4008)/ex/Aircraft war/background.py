# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 02:29:14 2020

@author: Wyh
"""

import pygame
from pygame.sprite import Sprite

# Set the background image. 
class Background(Sprite):
    
    def __init__(self, image_file, location):
        # Call Sprite initializer
        super().__init__()
        self.image = pygame.image.load('background.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
