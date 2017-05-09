'''
Created on Apr 03, 2017

@author: Brendan Hassler
'''

from enum import Enum

from random import random

class Bats(Enum):
    
    LEFT   = "Left"
    RIGHT  = "Right"
    SWITCH = "Switch"

    def __str__(self): return str(self.value)

class Throws(Enum):
    
    LEFT   = "Left"
    RIGHT  = "Right"

    def __str__(self): return str(self.value)


def generate_bats_throws():
	r_throws = random()
	r_bats   = random()

	if r_bats < 0.41:
		if r_throws < 0.366: return Bats.LEFT, Throws.LEFT
		else: return Bats.LEFT, Throws.RIGHT
	elif r_bats >= 0.41 and r_bats < 0.96:
		if r_throws < 0.182: return Bats.RIGHT, Throws.LEFT
		else: return Bats.RIGHT, Throws.RIGHT
	else:
		if r_throws < 0.5: return Bats.SWITCH, Throws.LEFT
		else: return Bats.SWITCH, Throws.RIGHT