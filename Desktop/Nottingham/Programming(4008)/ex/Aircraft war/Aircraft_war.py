# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:57:09 2020

@author: Wyh
"""

import pygame
from setting import Setting
from states import States
from rocket import Rocket
from button import Button
from scoreboard import Scoreboard
from textbox import Textbox
from incidents import Incidents
import functions
from pygame.sprite import Group

# Start main loop. 
def game_run():
    # Initialize and create screen. 
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("Aircraft war")
    
    # Create play button
    play_button = Button(setting, screen, 'Play', 200)
    help_button = Button(setting, screen, 'Help', 400)
    
    # Draw a rocket. 
    rocket = Rocket(setting, screen)
    
    # Set a Group for bullets. 
    bullets = Group()
    
    # Set a Group for alien bullets. 
    alien_bullets = Group()
    
    # Set a Group for aliens. 
    aliens = Group()
    
    # Create aliens. 
    functions.create_aliens(setting, screen, rocket, aliens, alien_bullets)
    
    # Create States. 
    states = States(setting)
    
    # Create Scoreboard. 
    scoreboard = Scoreboard(setting, screen, states)
    
    # Create Textbox. 
    textbox = Textbox(setting, screen)
    
    # Create Incidents. 
    incidents = Group()
    
    # Main loop. 
    while True:
        functions.respond_events(setting, screen, states, scoreboard, rocket, aliens, bullets, alien_bullets, play_button, help_button, textbox, incidents)
        if states.game_active:
            rocket.update_rocket()
            bullets.update(rocket)
            alien_bullets.update(setting)
            incidents.update(states)
            functions.update_bullets(setting, screen, states, scoreboard, rocket, aliens, bullets, alien_bullets)
            functions.update_aliens(setting, screen, states, scoreboard, rocket, aliens, bullets, alien_bullets, incidents)
            functions.update_alien_bullets(setting, screen, states, scoreboard, rocket, aliens, bullets, alien_bullets, incidents)
            functions.update_incidents(setting, screen, states, scoreboard, rocket, aliens, bullets, alien_bullets, incidents)
        functions.screen_update(setting, screen, states, scoreboard, rocket, aliens, bullets, alien_bullets, play_button, help_button, textbox, incidents)


game_run()