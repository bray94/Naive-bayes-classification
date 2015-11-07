from numpy import *

class numberClass(object):

	def __init__(self, value):
		self.classValue = value
		self.prior= .1
		self.empirical_likelihood = zeros((28,28))
		self.training_data = []

	def addTrainingData(self, training_value):
		self.training_data.append(training_value)

	def setPrior(self, priorValue):
		self.prior = priorValue

if __name__ == '__main__':
	main()
