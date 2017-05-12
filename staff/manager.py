import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'player_pkg'))

from random import random
from random import choice
from random import gauss

from namegen.namegen import rand_male_name
from namegen.namegen import rand_female_name
from namegen.namegen import rand_surname

from manager_birthday_gen import generate_birthdate
from manager_birthday_gen import years_old

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'calendar'))
from date import Day
from date import Month
from date import Date
from calendar_module import start_date

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'teams'))
from team import get_FA
from contract import Contract

class Manager():
	#Qualities to share with players should be
	#Name, Age, Contract
	#Attributes should be:
	#Organization, Discipline, Intelligence, Mentoring, Hitting Exp., Pitching Exp., Fielding Exp.

	def __init__(self, n, bd, org, dis, inl, men, hit, pit, fld, ctc):
		self.nameVar = n 
		self.birthdateVar = bd
		self.organizationVar = org
		self.disciplineVar = dis 
		self.intelligenceVar = inl
		self.mentoringVar = men
		self.hitting_experienceVar = hit
		self.pitching_experienceVar = pit
		self.fielding_experienceVar = fld
		self.contractVar = ctc

	def name(self): return self.nameVar
	def birthdate(self): return self.birthdateVar
	def organization(self): return self.organizationVar
	def discipline(self): return self.disciplineVar
	def intelligence(self): return self.intelligenceVar
	def mentoring(self): return self.mentoringVar
	def hitting_exp(self): return self.hitting_experienceVar
	def pitching_exp(self): return self.pitching_experienceVar
	def fielding_exp(self): return self.fielding_experienceVar
	def team(self): return self.contractVar.team()
	def contract(self): return self.contractVar

	def overall_rating(self): return int((self.organizationVar + self.disciplineVar + self.intelligenceVar + self.mentoringVar + self.hitting_experienceVar + self.pitching_experienceVar + self.fielding_experienceVar)/7.0)

	def __str__(self):
		info = self.name()
		info += ',' + str(self.birthdate())
		info += ',' + str(self.contract())
		info += ',Ovr: ' + str(self.overall_rating())
		return info


def generate_manager():
	r = random(); name = ''
	if r < 0.5: name = rand_male_name() + ' ' + rand_surname()
	else: name = rand_female_name() + ' ' + rand_surname()

	birthdate = generate_birthdate(start_date.year)

	qualities = []

	for param in params():
		qualities.append( redistribute(int(gauss(param[0], param[1]))) )

	contract = Contract(get_FA(), 0, 0)

	return Manager(name, birthdate, qualities[0], qualities[1], qualities[2], qualities[3], qualities[4], qualities[5], qualities[6], contract)

def params():
	bad = 20; poor = 40; okay = 60; good = 80; excellent = 100
	narrow = 3; medium = 6; wide = 10
	#Types of manager: bookworm, disciplinarian, veteran pitcher, active defender, easy rider, mentor, aggressive batsman, frugal spender
	bookworm = [(good, medium), (poor, wide), (excellent, narrow), (good, medium), (okay, wide), (okay, wide), (okay, wide)]
	disciplinarian = [(good, medium), (excellent, narrow), (okay, wide), (bad, medium), (okay, wide), (okay, wide), (okay, wide)]
	veteran_pitcher = [(okay, medium), (okay, narrow), (good, medium), (okay, wide), (poor, wide), (excellent, narrow), (okay, wide)]
	active_defender = [(okay, wide), (poor, wide), (okay, wide), (okay, wide), (poor, medium), (good, medium), (excellent, narrow)]
	easy_rider = [(poor, medium), (bad, narrow), (poor, medium), (good, wide), (okay, wide), (okay, wide), (okay, wide)]
	mentor = [(good, medium), (poor, wide), (good, wide), (excellent, narrow), (okay, wide), (okay, wide), (okay, wide)]
	aggressive_batsman = [(poor, wide), (okay, wide), (poor, medium), (poor, wide), (excellent, narrow), (poor, wide), (poor, wide)]
	frugal_spender = [(excellent, narrow), (okay, wide), (good, medium), (poor, medium), (okay, wide), (okay, wide), (okay, wide)]

	types = [bookworm, disciplinarian, veteran_pitcher, active_defender, easy_rider, mentor, aggressive_batsman, frugal_spender]

	return choice(types)

def redistribute(var):
	if var > 100: return 100
	if var < 0: return 0
	return var

for i in range(0, 30):
	print(generate_manager())