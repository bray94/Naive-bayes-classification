from numpy import *
from numberClass import *

def mapEstimate(possibleNumber, testData):

	prior = possibleNumber.prior

	total_likelihood = sum(sum(testData * possibleNumber.empirical_likelihood))

	return prior*total_likelihood

def numClassifier(classList, testData):
	list = zeros(10)

	for x in xrange(0,10):
		list[x] = mapEstimate(classList[x], testData)

	return argmax(list)

