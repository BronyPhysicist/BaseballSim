from random import random
from random import gauss

from namegen.namegen import rand_male_name
from namegen.namegen import rand_female_name
from namegen.namegen import rand_surname

from position import Pos

from height_weight_gen import catcher_height_weight
from height_weight_gen import infield_height_weight
from height_weight_gen import outfield_height_weight
from height_weight_gen import pitcher_height_weight

from birthday_gen import generate_birthdate
from birthday_gen import years_old
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'calendar'))
from date import Day
from date import Month
from date import Date
from calendar_module import start_date

from bats_and_throws import Bats
from bats_and_throws import Throws
from bats_and_throws import generate_bats_throws

from capabilities import Capabilities

from position_capabilities import PositionCapabilities

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'teams'))
from team import get_FA
from contract import Contract

class Player():

	#contains name, pos, height, weight, birthdate, bats, throws, caps, pos_caps, team, contract
	def __init__(self, n, p, h, w, bd, b, t, c, pc, ct):
		self.nameK = 'name'; self.posK = 'pos'; self.heightK = 'height'; self.weightK = 'weight'; self.birthdateK = 'birthdate'
		self.batsK = 'bats'; self.throwsK = 'throws'; self.capsK = 'caps'; self.pos_capsK = 'pos_caps'; self.contractK = 'contract'

		ess = {}
		ess[self.nameK] = n; ess[self.posK] = p; ess[self.heightK] = h; ess[self.weightK] = w; ess[self.birthdateK] = bd; ess[self.batsK] = b;
		ess[self.throwsK] = t; ess[self.capsK] = c; ess[self.pos_capsK] = pc; ess[self.contractK] = ct
		self.ess_dict = ess

	def name(self): return self.ess_dict[self.nameK]
	def pos(self): return self.ess_dict[self.posK]
	def height(self): return self.ess_dict[self.heightK]
	def weight(self): return self.ess_dict[self.weightK]
	def birthdate(self): return self.ess_dict[self.birthdateK]
	def bats(self): return self.ess_dict[self.batsK]
	def throws(self): return self.ess_dict[self.throwsK]
	def caps(self): return self.ess_dict[self.capsK]
	def pos_caps(self): return self.ess_dict[self.pos_capsK]
	def team(self): return self.ess_dict[self.contractK].team()
	def contract(self): return self.ess_dict[self.contractK]

	def overall_rating(self): return self.caps().overall_rating(self.pos())
	def overall_rating_new_pos(self, pos): return self.caps().overall_rating(pos)

	def __str__(self):
		info = self.name()
		info += ',' + str(self.pos())
		info += ',' + str(self.height()) + ',' + str(self.weight())
		info += ',' + str(self.birthdate())
		info += ',' + str(self.bats()) + ',' + str(self.throws())
		#info += ',' + str(self.caps()) + ',' + str(self.pos_caps())
		info += ',' + str(self.contract())
		info += ',Ovr: ' + str(self.overall_rating())
		return info

def generate_player():
	r = random(); name = ''
	if r < 0.5: name = rand_male_name() + ' ' + rand_surname()
	else: name = rand_female_name() + ' ' + rand_surname()

	pos = Pos.rand_position()

	weight, height = 0, 0
	if pos == Pos.CATCHER: weight, height = catcher_height_weight()
	elif Pos.is_infield(pos): weight, height = infield_height_weight()
	elif Pos.is_outfield(pos): weight, height = outfield_height_weight()
	else: weight, height = pitcher_height_weight()

	birthdate = generate_birthdate(start_date.year)

	bats, throws = generate_bats_throws()

	years_in_majors = int( gauss(years_old(birthdate, start_date) - 23, 2) )
	if years_in_majors < 0: years_in_majors = 0
	caps = Capabilities.generate_all_caps(height, weight, birthdate, start_date, years_in_majors, pos)

	pos_caps = PositionCapabilities.generate_pos_caps(pos)

	contract = Contract(get_FA(), 0, 0)
 
	return Player(name, pos, height, weight, birthdate, bats, throws, caps, pos_caps, contract)