# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 04:47:14 2020

@author: Wyh
"""

class States():
    
    # Initialize the game status that may change depending on the game. 
    def __init__(self, setting):
        self.setting = setting
        self.reset_states()
        self.game_active = False
        self.textbox_show = False
        self.create_incident = False
        self.incident_show = False
        self.highest_score = 0

    # Initializes statistics that may change depending on the game. 
    def reset_states(self):
        self.rocket_left = self.setting.rocket_lives
        self.score = 0