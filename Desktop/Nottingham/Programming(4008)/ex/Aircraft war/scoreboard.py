# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 03:19:02 2020

@author: Wyh
"""

import pygame.font
from pygame.sprite import Group
from rocket import Rocket

class Scoreboard():
    
    def __init__(self, setting, screen, states):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting = setting
        self.states = states
    
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_score()
        self.prep_highest_score()
        
        self.prep_rockets()
        
    def prep_score(self):
        score_str = str(self.states.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.setting.background_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_highest_score(self):
        highest_score = int(round(self.states.highest_score, -1))
        highest_score_str = "{:,}".format(highest_score)
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.setting.background_color)
        
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = self.score_rect.top
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.rockets.draw(self.screen)
    
    def prep_rockets(self):
        self.rockets = Group()
        for rocket_number in range(self.states.rocket_left):
            rocket = Rocket(self.setting, self.screen)
            rocket.rect.x = 10 + rocket_number * rocket.rect.width
            rocket.rect.y = 10
            self.rockets.add(rocket)
            