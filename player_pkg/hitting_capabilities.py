class HittingCapabilities():
	"""Contains: power, contact, bat speed, pitch recognition, bunt"""
	def __init__(self, power, contact, bat_speed, pitch_recognition, bunt):
		self.power = power								#Physical/Muscle
		self.contact = contact							#Training
		self.bat_speed = bat_speed						#Physical/Muscle
		self.pitch_recognition = pitch_recognition		#Mental/Sharpness
		self.bunt = bunt								#Training

	def __str__(self):
		info = str(self.power)
		info += ',' + str(self.contact)
		info += ',' + str(self.bat_speed)
		info += ',' + str(self.pitch_recognition)
		info += ',' + str(self.bunt)
		return info