class FieldingCapabilities():
	"""Contains: range, glove, throw range, throw speed, accuracy, jump"""
	def __init__(self, fld_range, glove, throw_range, throw_speed, accuracy, jump):
		self.field_range = fld_range		#Physical/Agility
		self.glove = glove					#Training
		self.throw_range = throw_range		#Physical/Muscle
		self.throw_speed = throw_speed		#Physical/Muscle
		self.accuracy = accuracy			#Training
		self.jump = jump					#Physical/Reflexes

	def __str__(self):
		info = str(self.field_range)
		info += ',' + str(self.glove)
		info += ',' + str(self.throw_range)
		info += ',' + str(self.throw_speed)
		info += ',' + str(self.accuracy)
		info += ',' + str(self.jump)
		return info
	