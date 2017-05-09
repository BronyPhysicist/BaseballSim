class PitchingCapabilities():
	"""Contains: stamina, arm strength, arm speed, pitch accuracy, spin, focus, pickoff"""
	def __init__(self, stamina, arm_strength, arm_speed, pitch_accuracy, spin, focus, pickoff):
		self.stamina = stamina					#Physical/Muscle
		self.arm_strength = arm_strength		#Physical/Muscle
		self.arm_speed = arm_speed				#Physical/Agility
		self.pitch_accuracy = pitch_accuracy	#Training
		self.spin = spin						#Training
		self.focus = focus						#Mental/Calmness
		self.pickoff = pickoff					#Mental/Strategy

	def __str__(self):
		info = str(self.stamina)
		info += ',' + str(self.arm_strength)
		info += ',' + str(self.arm_speed)
		info += ',' + str(self.pitch_accuracy)
		info += ',' + str(self.spin)
		info += ',' + str(self.focus)
		info += ',' + str(self.pickoff)
		return info