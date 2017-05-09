from division import div_from_abbrev
from division import Division

class Team():

	def __init__(self, city, name, abbrev, div, rivals, last_seas_wl):
		self.city = city
		self.name = name
		self.abbrev = abbrev
		self.div = div
		self.rivals = rivals
		self.last_seas_wl = last_seas_wl
		self.roster = []
		self.budget = 0

	def add_player(self, player): self.roster.append(player)
	def remove_player(self, player): self.roster.remove(player) 

	def __str__(self): return self.city + ' ' + self.name
	def abbr(self): return self.abbrev
	def __eq__(self, other): return (self.city == other.city) and (self.name == other.name)
	def __ne__(self, other): return (not (self.city == other.city)) or (not (self.name == other.name))


#HELPER METHODS

def team_list():
	f = open('../TextDocs/cities.csv')
	teams = []
	for line in f.readlines():
		data = line.split(',')
		if 'Free Agents' in data[0]:
			team = Team('Free Agents', '', 'FA', None, ['','',''], (0,0))
			teams.append(team)
		else:
			team = Team(data[0], data[1], data[2], div_from_abbrev(data[4]), [data[5], data[6], data[7]], (int(data[8]), int(data[9])))
			teams.append(team)
	f.close()
	return teams

TEAM_LIST = team_list()

def get_FA(): return TEAM_LIST[-1]

def team_list_no_FA():
	tl = TEAM_LIST
	to_remove = 0
	for team in tl:
		if team.city == 'Free Agents': to_remove = team
	tl.remove(to_remove)
	return tl