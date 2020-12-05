# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 04:47:14 2020

@author: Wyh
"""

class States():
    
    def __init__(self, setting):
        self.setting = setting
        self.reset_states()
        self.game_active = False
    
    def reset_states(self):
        self.rocket_left = self.setting.rocket_lives
        self.score = 0
        self.highest_score = 0