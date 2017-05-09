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

	def __init__(self, player_pos):
		self.skill_set = {}
		self.skill_set[Pos.CATCHER]      = redistribute(int(gauss(skill_levels[Pos.compare_pos(player_pos, Pos.CATCHER)], sigma)      ))
		self.skill_set[Pos.FIRST_BASE]   = redistribute(int(gauss(skill_levels[Pos.compare_pos(player_pos, Pos.FIRST_BASE)], sigma)   ))
		self.skill_set[Pos.SECOND_BASE]  = redistribute(int(gauss(skill_levels[Pos.compare_pos(player_pos, Pos.SECOND_BASE)], sigma)  ))
		self.skill_set[Pos.THIRD_BASE]   = redistribute(int(gauss(skill_levels[Pos.compare_pos(player_pos, Pos.THIRD_BASE)], sigma)   ))
		self.skill_set[Pos.SHORTSTOP]    = redistribute(int(gauss(skill_levels[Pos.compare_pos(player_pos, Pos.SHORTSTOP)], sigma)    ))
		self.skill_set[Pos.LEFT_FIELD]   = redistribute(int(gauss(skill_levels[Pos.compare_pos(player_pos, Pos.LEFT_FIELD)], sigma)   ))
		self.skill_set[Pos.CENTER_FIELD] = redistribute(int(gauss(skill_levels[Pos.compare_pos(player_pos, Pos.CENTER_FIELD)], sigma) ))
		self.skill_set[Pos.RIGHT_FIELD]  = redistribute(int(gauss(skill_levels[Pos.compare_pos(player_pos, Pos.RIGHT_FIELD)], sigma)  ))

	def redistribute(value):
		if value > MAX_VALUE: return MAX_VALUE
		elif value < MIN_VALUE: return MIN_VALUE
		else: return value

	def __str__(self):
		return str(self.skill_set)

table  = []; n = 0
for pos1 in Pos.pos_list_no_pitchers():
	table.append([])
	row_tot = 0
	for pos2 in Pos.pos_list_no_pitchers():
		row_tot += Pos.compare_pos(pos1, pos2)
		table[n].append(Pos.compare_pos(pos1, pos2))
	print(str(pos1) + ': ' + str(table[n]) + ' Total: ' + str(row_tot))
	n += 1
