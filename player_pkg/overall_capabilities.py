class OverallCapabilities():

	"""Contains: composure, judgment, reaction, memory, run_speed, acceleration, slide, awareness, patience"""
	def __init__(self, composure, judgment, reaction, memory, run_speed, acceleration, slide, awareness, patience):
		self.composure = composure			#Mental/Calmness
		self.judgment = judgment			#Mental/Sharpness
		self.reaction = reaction			#Physical/Reflexes
		self.memory = memory				#Mental/Sharpness
		self.run_speed = run_speed			#Physical/Agility
		self.acceleration = acceleration	#Physical/Agility
		self.slide = slide					#Physical/Reflexes
		self.awareness = awareness			#Mental/Sharpness
		self.patience = patience			#Mental/Calmness

	def rating(self, position):
		pass

	def __str__(self):
		info = str(self.composure)
		info += ',' + str(self.judgment)
		info += ',' + str(self.reaction)
		info += ',' + str(self.memory)
		info += ',' + str(self.run_speed)
		info += ',' + str(self.acceleration)
		info += ',' + str(self.slide)
		info += ',' + str(self.awareness)
		info += ',' + str(self.patience)
		return info