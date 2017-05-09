import attributes as attr
from overall_capabilities import OverallCapabilities as OC 
from hitting_capabilities import HittingCapabilities as HC 
from fielding_capabilities import FieldingCapabilities as FC 
from pitching_capabilities import PitchingCapabilities as PC 

from position import Pos

from random import choice
from random import gauss

class Capabilities():

	mus = 'muscle';    agi = 'agility';  ref = 'reflexes'
	sha = 'sharpness'; sta = 'strategy'; cal = 'calmness'
	hit = 'hitting';   fie = 'fielding'; pit = 'pitching'

	STDEVS = [2, 4, 6, 8, 10]

	MAX_VALUE = 100
	MIN_VALUE = 12

	def __init__(self, o_caps, h_caps, f_caps, p_caps):
		self.overall_capabilities  = o_caps
		self.hitting_capabilities  = h_caps
		self.fielding_capabilities = f_caps
		self.pitching_capabilities = p_caps

	@classmethod
	def weights(cls, position):
		if position == Pos.CATCHER:
			return [4, 8, 8, 5, 3, 3, 2, 7, 2, 5, 7, 6, 3, 1, 1, 10, 9, 10, 10, 1, 0, 0, 0, 0, 0, 0, 0]
		if position == Pos.FIRST_BASE or position == Pos.THIRD_BASE:
			return [1, 3, 4, 2, 7, 6, 5, 3, 3, 10, 10, 10, 8, 1, 2, 5, 7, 9, 8, 1, 0, 0, 0, 0, 0, 0, 0]
		if position == Pos.SECOND_BASE or position == Pos.SHORTSTOP:
			return [1, 3, 10, 1, 9, 7, 2, 8, 2, 3, 5, 5, 4, 1, 3, 8, 7, 10, 10, 6, 0, 0, 0, 0, 0, 0, 0]
		if position == Pos.LEFT_FIELD:
			return [1, 3, 4, 2, 7, 6, 5, 3, 3, 10, 10, 10, 8, 1, 2, 5, 7, 9, 8, 1, 0, 0, 0, 0, 0, 0, 0]
		if position == Pos.CENTER_FIELD:
			return [1, 7, 8, 2, 10, 8, 4, 9, 5, 2, 7, 6, 1, 1, 10, 10, 3, 3, 3, 5, 0, 0, 0, 0, 0, 0, 0]
		if position == Pos.RIGHT_FIELD:
			return [1, 2, 5, 2, 6, 4, 3, 5, 1, 8, 10, 10, 3, 1, 7, 7, 10, 9, 8, 3, 0, 0, 0, 0, 0, 0, 0]
		if position == Pos.STARTER:
			return [6, 7, 2, 2, 4, 2, 1, 5, 2, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 10, 10, 6, 9, 8, 8, 4]
		if position == Pos.LONG_RELIEF:
			return [8, 9, 2, 2, 4, 2, 1, 5, 2, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 8, 10, 6, 10, 6, 7, 4]
		if position == Pos.MIDDLE_RELIEF:
			return [10, 8, 2, 2, 4, 2, 1, 5, 2, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 6, 8, 10, 7, 6, 9, 4]
		if position == Pos.CLOSER:
			return [10, 8, 2, 2, 4, 2, 1, 8, 2, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 5, 7, 10, 6, 6, 9, 4]

	@classmethod
	def redistribute(cls, skill):
		if skill > cls.MAX_VALUE: return cls.MAX_VALUE
		elif skill < cls.MIN_VALUE: return cls.MIN_VALUE
		else: return skill

	@classmethod
	def set_of_attrs(cls, height, weight, birthdate, current_date, years_in_majors, position):
		atts = {}
		atts[cls.mus] = attr.generate_muscle_stat(height, weight)
		atts[cls.agi] = attr.generate_agility_stat(height, weight, birthdate, current_date)
		atts[cls.ref] = attr.generate_reflexes_stat(birthdate, current_date)
		atts[cls.sha] = attr.generate_mental_stat()
		atts[cls.sta] = attr.generate_mental_stat()
		atts[cls.cal] = attr.generate_mental_stat()
		atts[cls.hit], atts[cls.fie], atts[cls.pit] = attr.generate_training_stats(years_in_majors, position)
		return atts

	@classmethod
	def generate_all_caps(cls, height, weight, birthdate, current_date, years_in_majors, position):
		atts = cls.set_of_attrs(height, weight, birthdate, current_date, years_in_majors, position)

		#Overall
		composure    = cls.redistribute( int( gauss(atts[cls.cal], choice(cls.STDEVS)) ) )
		judgment     = cls.redistribute( int( gauss(atts[cls.sha], choice(cls.STDEVS)) ) )
		reaction     = cls.redistribute( int( gauss(atts[cls.ref], choice(cls.STDEVS)) ) )
		memory       = cls.redistribute( int( gauss(atts[cls.sha], choice(cls.STDEVS)) ) )
		run_speed    = cls.redistribute( int( gauss(atts[cls.agi], choice(cls.STDEVS)) ) )
		acceleration = cls.redistribute( int( gauss(atts[cls.agi], choice(cls.STDEVS)) ) )
		slide        = cls.redistribute( int( gauss(atts[cls.ref], choice(cls.STDEVS)) ) )
		awareness    = cls.redistribute( int( gauss(atts[cls.sha], choice(cls.STDEVS)) ) )
		patience     = cls.redistribute( int( gauss(atts[cls.cal], choice(cls.STDEVS)) ) )
		ocs = OC(composure, judgment, reaction, memory, run_speed, acceleration, slide, awareness, patience)

		#Hitting
		power             = cls.redistribute( int( gauss(atts[cls.mus], choice(cls.STDEVS)) ) )
		contact           = cls.redistribute( int( gauss(atts[cls.hit], choice(cls.STDEVS)) ) )
		bat_speed         = cls.redistribute( int( gauss(atts[cls.mus], choice(cls.STDEVS)) ) )
		pitch_recognition = cls.redistribute( int( gauss(atts[cls.sha], choice(cls.STDEVS)) ) )
		bunt              = cls.redistribute( int( gauss(atts[cls.hit], choice(cls.STDEVS)) ) )
		hcs = HC(power, contact, bat_speed, pitch_recognition, bunt)

		#Fielding
		field_range = cls.redistribute( int( gauss(atts[cls.agi], choice(cls.STDEVS)) ) )
		glove       = cls.redistribute( int( gauss(atts[cls.fie], choice(cls.STDEVS)) ) )
		throw_range = cls.redistribute( int( gauss(atts[cls.mus], choice(cls.STDEVS)) ) )
		throw_speed = cls.redistribute( int( gauss(atts[cls.mus], choice(cls.STDEVS)) ) )
		accuracy    = cls.redistribute( int( gauss(atts[cls.fie], choice(cls.STDEVS)) ) )
		jump        = cls.redistribute( int( gauss(atts[cls.ref], choice(cls.STDEVS)) ) )
		fcs = FC(field_range, glove, throw_range, throw_speed, accuracy, jump)

		#Pitching 
		pcs = 0
		if Pos.is_pitcher(position):
			stamina        = cls.redistribute( int( gauss(atts[cls.mus], choice(cls.STDEVS)) ) )
			arm_strength   = cls.redistribute( int( gauss(atts[cls.mus], choice(cls.STDEVS)) ) )
			arm_speed      = cls.redistribute( int( gauss(atts[cls.agi], choice(cls.STDEVS)) ) )
			pitch_accuracy = cls.redistribute( int( gauss(atts[cls.pit], choice(cls.STDEVS)) ) )
			spin           = cls.redistribute( int( gauss(atts[cls.pit], choice(cls.STDEVS)) ) )
			focus          = cls.redistribute( int( gauss(atts[cls.cal], choice(cls.STDEVS)) ) )
			pickoff        = cls.redistribute( int( gauss(atts[cls.sta], choice(cls.STDEVS)) ) )
			pcs = PC(stamina, arm_strength, arm_speed, pitch_accuracy, spin, focus, pickoff)
		else:
			stamina        = cls.redistribute( int( gauss(cls.MIN_VALUE, 2) ) )
			arm_strength   = cls.redistribute( int( gauss(cls.MIN_VALUE, 2) ) )
			arm_speed      = cls.redistribute( int( gauss(cls.MIN_VALUE, 2) ) )
			pitch_accuracy = cls.redistribute( int( gauss(cls.MIN_VALUE, 2) ) )
			spin           = cls.redistribute( int( gauss(cls.MIN_VALUE, 2) ) )
			focus          = cls.redistribute( int( gauss(cls.MIN_VALUE, 2) ) )
			pickoff        = cls.redistribute( int( gauss(cls.MIN_VALUE, 2) ) )
			pcs = PC(stamina, arm_strength, arm_speed, pitch_accuracy, spin, focus, pickoff)

		return Capabilities(ocs, hcs, fcs, pcs)

	def overall_rating(self, position):
		w = Capabilities.weights(position)
		tot = w[0] *self.overall_capabilities.composure         + w[1] *self.overall_capabilities.judgment     + w[2] *self.overall_capabilities.reaction        \
			+ w[3] *self.overall_capabilities.memory            + w[4] *self.overall_capabilities.run_speed    + w[5] *self.overall_capabilities.acceleration    \
			+ w[6] *self.overall_capabilities.slide             + w[7] *self.overall_capabilities.awareness    + w[8] *self.overall_capabilities.patience        \
			+ w[9] *self.hitting_capabilities.power             + w[10]*self.hitting_capabilities.contact      + w[11]*self.hitting_capabilities.bat_speed       \
			+ w[12]*self.hitting_capabilities.pitch_recognition + w[13]*self.hitting_capabilities.bunt         + w[14]*self.fielding_capabilities.field_range    \
			+ w[15]*self.fielding_capabilities.glove            + w[16]*self.fielding_capabilities.throw_range + w[17]*self.fielding_capabilities.throw_speed    \
			+ w[18]*self.fielding_capabilities.accuracy         + w[19]*self.fielding_capabilities.jump        + w[20]*self.pitching_capabilities.stamina        \
			+ w[21]*self.pitching_capabilities.arm_strength     + w[22]*self.pitching_capabilities.arm_speed   + w[23]*self.pitching_capabilities.pitch_accuracy \
			+ w[24]*self.pitching_capabilities.spin             + w[25]*self.pitching_capabilities.focus       + w[26]*self.pitching_capabilities.pickoff
		return tot/sum(w)

	def __str__(self):
		return str(self.overall_capabilities) + '/' + str(self.hitting_capabilities) + '/' + str(self.fielding_capabilities) + '/' + str(self.pitching_capabilities)