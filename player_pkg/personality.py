from random import random
from enum import Enum

class Personality(Enum):
    RL = ('Respected Leader',    [3,2,2,1,2,1,1,2], 0.06)
    MD = ('Media Darling',       [3,2,1,2,2,1,2,2], 0.065)
    DW = ('Disciplined Worker',  [2,1,1,3,3,3,1,2], 0.075)
    PT = ('Patient Teacher',     [3,1,2,2,3,2,2,1], 0.07)
    QN = ('Quiet Nurturer',      [1,3,1,1,2,2,5,3], 0.08)
    OH = ('Oblivious Happy Guy', [3,3,3,2,1,1,3,5], 0.11)
    CT = ('Cold Thinker',        [3,2,2,3,4,4,5,1], 0.09)
    ND = ('Nondescript',         [3,3,3,3,3,3,3,3], 0.2)
    BT = ('Brawny Tough-Guy',    [4,4,5,4,2,3,3,5], 0.12)
    IF = ('Impusive Fighter',    [3,4,5,4,4,4,4,3], 0.07)
    AB = ('Angry Bigot',         [4,3,5,5,5,5,4,4], 0.03)
    EG = ('Egomaniac',           [5,5,5,4,3,5,4,4], 0.03)

    def name(self): return self.value[0]
    def pers_array(self): return self.value[1]
    def prob(self): return self.value[2]

    def ego(self): return self.value[1][0]
    def discipline(self): return self.value[1][1]
    def temper(self): return self.value[1][2]
    def tolerance(self): return self.value[1][3]
    def optimism(self): return self.value[1][4]
    def charm(self): return self.value[1][5]
    def leadership(self): return self.value[1][6]
    def intellect(self): return self.value[1][7]

    def __str__(self): return self.name()

    @classmethod
    def personality_list(cls):
    	return [cls.RL, cls.MD, cls.DW, cls.PT, cls.QN, cls.OH, cls.CT, cls.ND, cls.BT, cls.IF, cls.AB, cls.EG]

    @classmethod
    def rand_personality(cls):
    	pers_list = cls.personality_list()
    	r = random()
    	p_sum = 0
    	for pers in pers_list:
    		p_sum += pers.prob()
    		if r < p_sum: return pers
    	return pers_list[0]