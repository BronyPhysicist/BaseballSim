'''
Created on Jun 9, 2016

@author: Brendan Hassler
'''
from enum import Enum
class Position(Enum):
    
    CATCHER = "C"
    FIRSTBASE = "1B"
    SECONDBASE = "2B"
    SHORTSTOP = "SS"
    THIRDBASE = "3B"
    LEFTFIELD = "LF"
    CENTERFIELD = "CF"
    RIGHTFIELD = "RF"
    STARTER = "SP"
    LONGRELIEF = "LRP"
    MIDDLERELIEF = "MRP"
    CLOSER = "CL"
    DESIGNATEDHITTER = "DH"
    
    @classmethod
    def compare_pos(cls, pos1, pos2):
        infield    = [cls.FIRSTBASE, cls.SECONDBASE, cls.SHORTSTOP, cls.THIRDBASE]
        outfield   = [cls.LEFTFIELD, cls.CENTERFIELD, cls.RIGHTFIELD]
        left_side  = [cls.LEFTFIELD, cls.THIRDBASE, cls.SHORTSTOP]
        center     = [cls.SECONDBASE, cls.CENTERFIELD]
        right_side = [cls.FIRSTBASE, cls.RIGHTFIELD]
        pitchers   = [cls.STARTER, cls.LONGRELIEF, cls.MIDDLERELIEF, cls.CLOSER]
        batters    = [cls.CATCHER, cls.FIRSTBASE, cls.SECONDBASE, cls.SHORTSTOP, cls.THIRDBASE, cls.LEFTFIELD, cls.CENTERFIELD, cls.RIGHTFIELD, cls.DESIGNATEDHITTER]
        
        score = 0
        
        if pos1 == pos2: return 4
        if pos1 in pitchers and pos2 in batters: return 1
        if pos1 == cls.CATCHER and pos2 in infield: return 2
        if pos1 != cls.CATCHER and pos2 == cls.CATCHER: return 0
        
        if pos1 in  infield and pos2 in infield: score += 2
        if pos1 in outfield and pos2 in outfield: score += 3
        if (pos1 == cls.FIRSTBASE and pos2 == cls.THIRDBASE) or (pos1 == cls.THIRDBASE and pos2 == cls.FIRSTBASE): score += 1
        if (pos1 == cls.SHORTSTOP and pos2 in outfield) or (pos1 in outfield and pos2 == cls.SHORTSTOP): score += 1
        if (pos1 == cls.SECONDBASE and pos2 == cls.SHORTSTOP) or (pos1 == cls.SHORTSTOP and pos2 == cls.SECONDBASE): score += 1
        if pos1 in left_side and pos2 in left_side: score += 1
        if pos1 in center and pos2 in center: score += 1
        if pos1 in right_side and pos2 in right_side: score += 1
        
        return score
        