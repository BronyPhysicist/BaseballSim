import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'teams'))
from team import get_FA

class Contract():

	def __init__(self, team, salary, years):
		self.team = team
		self.salary = salary
		self.years = years

	def __str__(self):
		fa = get_FA()
		if fa == self.team: return 'Unsigned.'
		else: return 'Signed with the ' + str(self.team) + ' for $' + str(self.salary) + ' over ' + str(self.years) + ' years.'