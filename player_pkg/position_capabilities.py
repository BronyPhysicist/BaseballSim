from position import Pos

from random import gauss

class PositionCapabilities():
	MAX_VALUE = 100
	skilled	  = 85
	competent = 70
	unskilled = 50
	poor      = 36
	bad		  = 20
	MIN_VALUE = 12

	skill_levels = [bad, poor, unskilled, competent, skilled, MAX_VALUE]

	sigma = 4

	def __init__(self, skill_set):
		self.skill_set = skill_set

	@classmethod
	def generate_pos_caps(cls, player_pos):
		skills = {}
		skills[Pos.CATCHER]      = cls.redistribute(int(gauss(cls.skill_levels[Pos.compare_pos(player_pos, Pos.CATCHER)],      cls.sigma) ))
		skills[Pos.FIRST_BASE]   = cls.redistribute(int(gauss(cls.skill_levels[Pos.compare_pos(player_pos, Pos.FIRST_BASE)],   cls.sigma) ))
		skills[Pos.SECOND_BASE]  = cls.redistribute(int(gauss(cls.skill_levels[Pos.compare_pos(player_pos, Pos.SECOND_BASE)],  cls.sigma) ))
		skills[Pos.THIRD_BASE]   = cls.redistribute(int(gauss(cls.skill_levels[Pos.compare_pos(player_pos, Pos.THIRD_BASE)],   cls.sigma) ))
		skills[Pos.SHORTSTOP]    = cls.redistribute(int(gauss(cls.skill_levels[Pos.compare_pos(player_pos, Pos.SHORTSTOP)],    cls.sigma) ))
		skills[Pos.LEFT_FIELD]   = cls.redistribute(int(gauss(cls.skill_levels[Pos.compare_pos(player_pos, Pos.LEFT_FIELD)],   cls.sigma) ))
		skills[Pos.CENTER_FIELD] = cls.redistribute(int(gauss(cls.skill_levels[Pos.compare_pos(player_pos, Pos.CENTER_FIELD)], cls.sigma) ))
		skills[Pos.RIGHT_FIELD]  = cls.redistribute(int(gauss(cls.skill_levels[Pos.compare_pos(player_pos, Pos.RIGHT_FIELD)],  cls.sigma) ))
		return PositionCapabilities(skills)

	@classmethod
	def redistribute(cls, value):
		if value > cls.MAX_VALUE: return cls.MAX_VALUE
		elif value < cls.MIN_VALUE: return cls.MIN_VALUE
		else: return value

	def __str__(self):
		return str(self.skill_set)

'''
table  = []; n = 0
for pos1 in Pos.pos_list_no_pitchers():
	table.append([])
	row_tot = 0
	for pos2 in Pos.pos_list_no_pitchers():
		row_tot += Pos.compare_pos(pos1, pos2)
		table[n].append(Pos.compare_pos(pos1, pos2))
	print(str(pos1) + ': ' + str(table[n]) + ' Total: ' + str(row_tot))
	n += 1
'''