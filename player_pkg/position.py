from enum import Enum

from random import random

class Pos(Enum):
	CATCHER       = 'C'
	FIRST_BASE    = '1B'
	SECOND_BASE   = '2B'
	THIRD_BASE    = '3B'
	SHORTSTOP     = 'SS'
	LEFT_FIELD    = 'LF'
	CENTER_FIELD  = 'CF'
	RIGHT_FIELD   = 'RF'
	STARTER       = 'SP'
	LONG_RELIEF   = 'LRP'
	MIDDLE_RELIEF = 'MRP'
	CLOSER        = 'CL'
	DESIG_HITTER  = 'DH'
    
	@classmethod
	def pos_list_with_DH(cls): return [cls.CATCHER, cls.FIRST_BASE, cls.SECOND_BASE, cls.THIRD_BASE, cls.SHORTSTOP, cls.LEFT_FIELD, cls.CENTER_FIELD, cls.RIGHT_FIELD, \
	cls.STARTER, cls.LONG_RELIEF, cls.MIDDLE_RELIEF, cls.CLOSER, cls.DESIG_HITTER]

	@classmethod
	def pos_list(cls): return Pos.pos_list_with_DH()[:-1]

	@classmethod
	def pos_list_no_pitchers(cls): return Pos.pos_list_with_DH()[0:8]

	@classmethod
	def is_batter(cls, pos):
		batters = cls.pos_list_no_pitchers(); batters.append(cls.DESIG_HITTER)
		if pos in batters: return True
		return False

	@classmethod
	def is_pitcher(cls, pos):
		pitchers = [cls.STARTER, cls.LONG_RELIEF, cls.MIDDLE_RELIEF, cls.CLOSER]
		if pos in pitchers: return True
		return False

	@classmethod
	def is_infield(cls, pos):
		infield = [cls.CATCHER, cls.FIRST_BASE, cls.SECOND_BASE, cls.SHORTSTOP, cls.THIRD_BASE]
		if pos in infield: return True
		return False

	@classmethod
	def is_outfield(cls, pos):
		outfield = [cls.LEFT_FIELD, cls.CENTER_FIELD, cls.RIGHT_FIELD]
		if pos in outfield: return True
		return False

	"""Should be read as: How well could a pos1 do a pos2\'s job?"""
	@classmethod
	def compare_pos(cls, pos1, pos2):
		infield    = [cls.FIRST_BASE, cls.SECOND_BASE, cls.SHORTSTOP, cls.THIRD_BASE]
		outfield   = [cls.LEFT_FIELD, cls.CENTER_FIELD, cls.RIGHT_FIELD]
		left_side  = [cls.LEFT_FIELD, cls.THIRD_BASE, cls.SHORTSTOP]
		center     = [cls.SECOND_BASE, cls.CENTER_FIELD]
		right_side = [cls.FIRST_BASE, cls.RIGHT_FIELD]
		bases      = [cls.FIRST_BASE, cls.SECOND_BASE, cls.THIRD_BASE]
		pitchers   = [cls.STARTER, cls.LONG_RELIEF, cls.MIDDLE_RELIEF, cls.CLOSER]
		batters    = [cls.CATCHER, cls.FIRST_BASE, cls.SECOND_BASE, cls.SHORTSTOP, cls.THIRD_BASE, cls.LEFT_FIELD, cls.CENTER_FIELD, cls.RIGHT_FIELD, cls.DESIG_HITTER]
		
		score = 0
		
		if pos1 == pos2: return 5
		if pos1 in pitchers and pos2 in batters: return 1
		if pos1 == cls.CATCHER and pos2 in infield: return 2
		if pos1 != cls.CATCHER and pos2 == cls.CATCHER: return 0
		if (pos1 in outfield and pos2 == cls.SHORTSTOP): return 2
		if (pos1 == cls.FIRST_BASE and pos2 == cls.THIRD_BASE) or (pos1 == cls.THIRD_BASE and pos2 == cls.FIRST_BASE): return 4
		
		if pos1 in  infield and pos2 in infield: score += 2
		if pos1 in outfield and pos2 in outfield: score += 4
		if pos1 in bases and pos2 in bases: score += 1
		if (pos1 == cls.SHORTSTOP and pos2 in outfield): score += 1
		if (pos1 == cls.SECOND_BASE and pos2 == cls.SHORTSTOP) or (pos1 == cls.SHORTSTOP and pos2 == cls.SECOND_BASE): score += 1
		if pos1 in left_side and pos2 in left_side: score += 1
		if pos1 in center and pos2 in center: score += 1
		if pos1 in right_side and pos2 in right_side: score += 1
		
		return score

	@classmethod
	def rand_position(cls):
		#Note: Probabilities subject to change
		probs = [0.089, 0.049, 0.055, 0.065, 0.057, 0.07, 0.06, 0.053, 0.205, 0.072, 0.171, 0.054]
		r = random()
		cum_prob = 0
		pos_choice = cls.pos_list()
		for n in range(0, len(pos_choice)):
			cum_prob += probs[n]
			if r < cum_prob: return pos_choice[n]
		return cls.CATCHER


	def __str__(self):
		return str(self.value)