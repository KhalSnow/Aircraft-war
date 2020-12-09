# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 03:35:55 2020

@author: Wyh
"""

import pygame.font

class Textbox():
    
    # Initialize textbox and its position. 
    def __init__(self, setting, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 100, 100
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,28)
        
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx = self.screen_rect.left + 100
        self.rect.centery = self.screen_rect.height / 2
        
        self.show_textbox()
        
    # Show textbox. 
    def show_textbox(self):
        textbox_str = "Press q to quit. Press space to fire bullet. Press w to go up. Press s to go down. Press a to go left. Press d to go right. "
        self.background_color = (0,255,255)
        self.textbox_image = self.font.render(textbox_str, True, self.text_color, self.background_color)
        self.textbox_image_rect = self.textbox_image.get_rect()
        self.textbox_image_rect.center = self.rect.center
        
    # Draw textbox.
    def draw_textbox(self):
        self.screen.blit(self.textbox_image, self.rect)