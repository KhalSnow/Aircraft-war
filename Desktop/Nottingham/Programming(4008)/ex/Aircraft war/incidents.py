# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 00:37:04 2020

@author: Wyh
"""

import pygame
from pygame.sprite import Sprite
import random

class Incidents(Sprite):
    
    def __init__(self, setting, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image_life_up = pygame.image.load("rocket_life_up.bmp")
        self.image_boom = pygame.image.load("boom.bmp")
        self.image, self.rand = self.get_image()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 0.5
        
        self.rect.centerx = random.randint(300,900)
        self.rect.centery = random.randint(200,600)
        
        self.incident_x = float(self.rect.x)
        self.incident_y = float(self.rect.y)
        
    def update(self, states):
        self.incident_x += random.randint(-1,1) * self.speed
        self.rect.x = self.incident_x
        self.incident_y += random.randint(-1,1) * self.speed
        self.rect.y = self.incident_y
    
    def get_image(self):
        rand = random.randint(1,2)
        if rand == 1:
            self.image = self.image_boom
        # elif rand == 2:
        #     self.image = self
        else:
            self.image = self.image_life_up
        return self.image, rand
    
    def blit(self):
        self.screen.blit(self.image, self.rect)