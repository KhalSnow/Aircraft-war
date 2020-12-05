# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:52:50 2020

@author: Wyh
"""

# A class to store all the settings of the game. 
class Setting():
    
    # Initialize the game's settings. 
    def __init__(self):
        # Screen setting. 
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230,230,230)
        
        # Rocket setting. 
        self.rocket_speed = 1.5
        self.rocket_lives = 3
        
        # Bullet setting. 
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_max = 3
        
        # Alien setting. 
        self.alien_speed = 0.5
        self.aliens_drop_speed = 5
        self.aliens_direction = 1
        self.alien_points = 50