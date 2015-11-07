

class Feature(object):
	
	#x_location;
	#y_location;
	#likelihood;
	#smoothed_likelihood;

	def __init__(self, x_loc, y_loc, value):
		self.x_location = x_loc
		self.y_location = y_loc
		self.value = value
