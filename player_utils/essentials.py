class Essentials():

	#contains name, pos, height, weight, birthdate, bats, throws, caps, pos_caps, team, contract

	name = 'name'; pos = 'pos'; height = 'height'; weight = 'weight'; birthdate = 'birthdate'; bats = 'bats'; throws = 'throws'
	caps = 'caps'; pos_caps = 'pos_caps'; team = 'team'; contract = 'contract'
	def __init__(n, p, h, w, bd, b, t, c, pc, tm, ct):
		ess = {}
		ess[name] = n; ess[pos] = p; ess[height] = h; ess[weight] = w; ess[birthdate] = bd; ess[bats] = b;
		ess[throws] = t; ess[caps] = c; ess[pos_caps] = pc; ess[team] = tm; ess[contract] = ct
		self.ess_dict = ess

	def name(self): return self.ess_dict[name]
	def pos(self): return self.ess_dict[pos]
	def height(self): return self.ess_dict[height]
	def weight(self): return self.ess_dict[weight]
	def birthdate(self): return self.ess_dict[birthdate]
	def bats(self): return self.ess_dict[bats]
	def throws(self): return self.ess_dict[throws]
	def caps(self): return self.ess_dict[caps]
	def pos_caps(self): return self.ess_dict[pos_caps]
	def team(self): return self.ess_dict[team]
	def contract(self): return self.ess_dict[contract]