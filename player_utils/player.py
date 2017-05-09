'''
Created on Jun 9, 2016

@author: Brendan Hassler
'''

import player_utils.position.Position as Position
import player_utils.bats.Bats as Bats
import player_utils.throws.Throws as Throws

from random import gauss

class Player:
    
    max_val = 0xFF
    start_valz = [0xF, 0x1F, 0x3F, 0x7F, 0xFF]
    #Attributes indices
    nam = 'NAME'; hgt = 'HEIGHT'; wgt = 'WEIGHT'; bts = 'BATS'; thr = 'THROWS'; bdy = 'BIRTHDATE'; pos = 'POSITION'
    
    def __init__(self, name, position, birthdate, attr):
        self.name = name
        self.pos = position
        self.birthdate = birthdate
        self.attr = attr
        
    
    def generate_pos_caps(self):
        pos_caps = {}
        for pos in Position:
            if pos == self.pos: pos_caps[pos] = Player.max_val
            else: pos_caps[pos] = Player.start_valz[Position.compare_pos(self.pos, pos)]
        return pos_caps
            
    def is_infield(self): return self.pos == Position.FIRSTBASE or self.pos == Position.SECONDBASE or self.pos == Position.SHORTSTOP or self.pos == Position.THIRDBASE
    
    def is_outfield(self): return self.pos == Position.LEFTFIELD or self.pos == Position.CENTERFIELD or self.pos == Position.RIGHTFIELD
        
    def is_catcher(self): return self.pos == Position.CATCHER
    
    def is_pitcher(self): return self.pos == Position.STARTER or self.pos == Position.LONGRELIEF or self.pos == Position.MIDDLERELIEF or self.pos == Position.CLOSER
        
        