from numpy import *
from numberClass import *

"""
This function computes the mapEstimate (posterior)
for a testimage and a potential class
testData = the test image to be classified
possibleNumber = numberClass object to which
		   this testimage might belong
"""
def mapEstimate(possibleNumber, testData):

	prior = possibleNumber.prior

	computedLikelihoods = possibleNumber.empirical_likelihood

	total_likelihood = 0

	for x in xrange(0,28):
		for y in xrange(0,28):
			if testData[x][y] == 0:
				total_likelihood += math.log(1 - computedLikelihoods[x][y])
			else:
				total_likelihood += math.log(computedLikelihoods[x][y])

	return math.log(prior) + total_likelihood

"""
This function assignes a testimage to the class
with the highest posterior
classList = an array of numberClass objects
testData = the input test image
"""
def numClassifier(classList, testData):
	list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	for x in xrange(0,10):
		list[x] = mapEstimate(classList[x], testData)

	assignedClass = list.index(max(list))

	if list[assignedClass] > classList[assignedClass].highestPosterior:
		classList[assignedClass].highestPosterior = list[assignedClass]
		classList[assignedClass].highPostImage = testData

	if list[assignedClass] < classList[assignedClass].lowestPosterior:
		classList[assignedClass].lowestPosterior = list[assignedClass]
		classList[assignedClass].lowPostImage = testData

	return assignedClass