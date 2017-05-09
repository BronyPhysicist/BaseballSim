from enum import Enum

class Division(Enum):
	ALEAST    = ("Alteran League East",     "AL East")
	ALCENTRAL = ("Alteran League Central",  "AL Central")
	ALWEST    = ("Alteran League West",     "AL West")
	NLEAST    = ("Nosteran League East",    "NL East")
	NLCENTRAL = ("Nosteran League Central", "NL Central")
	NLWEST    = ("Nosteran League West",    "NL West")

	def name(self): return self.value[0]
	def abbrev(self): return self.value[1]

	def __str__(self):
		return self.abbrev()

	@classmethod
	def al(cls): return [cls.ALEAST, cls.ALCENTRAL, cls.ALWEST]

	@classmethod
	def nl(cls): return [cls.NLEAST, cls.NLCENTRAL, cls.NLWEST]

	@classmethod
	def all_divs(cls): return [cls.ALEAST, cls.ALCENTRAL, cls.ALWEST, cls.NLEAST, cls.NLCENTRAL, cls.NLWEST]

	@classmethod
	def same_league(cls, div1, div2):
		return (div1 in cls.al() and div2 in cls.al()) or (div1 in cls.nl() and div2 in cls.nl())

    
def div_from_abbrev(abb):
	for div in Division.all_divs():
		if div.abbrev() == abb: return div
	return ''