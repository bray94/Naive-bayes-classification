from numpy import * 
from numberClass import *
from training import *
from testing import *

classes = (10)

def readTrainingLabels():
	# Open The File
	file = open("digitdata/traininglabels" , "r")

	# Count each digit in training set
	list = [0,0,0,0,0,0,0,0,0,0]
	labels = []

	# Total num of digits
	counter = 0

	for line in file:
		list[int(line.strip())]+=1
		counter+=1
		labels.append(int(line.strip()))

	file.close()

	return [float(x)/counter for x in list],labels

def readTrainingImages():
	# Open the Training Images
	file = open("digitdata/trainingimages", "r")

	# The List to store the images
	list = []

	curr_image = zeros((28,28))
	i = 0


	for line in file:
		# Remove the \n
		line = line.rstrip()

		j = 0

		for character in line:
			if line[j] != ' ':
				curr_image[(i)%28][j] = 1
			j+=1

		i+=1

		if (i%28) == 0:
			list.append(curr_image)
			curr_image = zeros((28,28))

	return list

def readTestingLabels():
	# Open The File
	file = open("digitdata/testlabels" , "r")

	# Count each digit in training set
	list = [0,0,0,0,0,0,0,0,0,0]
	labels = []

	# Total num of digits
	counter = 0

	for line in file:
		list[int(line.strip())]+=1
		counter+=1
		labels.append(int(line.strip()))

	file.close()

	return list,labels

def readTestingImages():
	# Open the Training Images
	file = open("digitdata/testimages", "r")

	# The List to store the images
	list = []
	list1 = []

	curr_image = zeros((28,28))
	curr_image_original = [[' ' for x in range(28)] for x in range(28)] 
	i = 0


	for line in file:
		# Remove the \n
		line = line.rstrip()

		j = 0

		for character in line:
			if line[j] == ' ':
				curr_image[(i)%28][j] = 0
				curr_image_original[(i)%28][j] = ' '
			elif line[j] == '+':
				curr_image[(i)%28][j] = 1
				curr_image_original[(i)%28][j] = '+'
			else:
				curr_image[(i)%28][j] = 1
				curr_image_original[(i)%28][j] = '#'

			j+=1

		i+=1

		if (i%28) == 0:
			list.append(curr_image)
			list1.append(curr_image_original)
			curr_image = zeros((28,28))
			curr_image_original = [[' ' for x in range(28)] for x in range(28)] 

	return list , list1


def main():
	#priorList = readTrainingLabels()
	imagesList = readTrainingImages()
	labelsList, labels = readTrainingLabels()

	classesList = []

	for x in xrange(0,10):
		classesList.append(numberClass(x))
		classesList[x].setPrior(labelsList[x])

	for x in xrange(0,len(imagesList)):
		classesList[labels[x]].addTrainingData(imagesList[x])



	for i in xrange(1,2):
		for x in xrange(0,10):
			classesList[x].empirical_likelihood = smoothed_likelihood(classesList[x].training_data,i)

		testingImagesList , originalTestingImagesList = readTestingImages()
		hypotheticalLabels = []
		confusionMatrix = zeros((10,10))

		for x in xrange(0, len(testingImagesList)):
			hypotheticalLabels.append(numClassifier(classesList,testingImagesList[x], originalTestingImagesList[x]))

		hypotheticalClasses = [0,0,0,0,0,0,0,0,0,0]
		for element in hypotheticalLabels:
			hypotheticalClasses[element]+=1

		#print hypotheticalClasses
		
		testClasses, testLabels = readTestingLabels()

		error = list(array(hypotheticalLabels) - array(testLabels))

		error_by_class = []
		for x in xrange(0,10):
			error_by_class.append(100 - abs(float(hypotheticalClasses[x]-testClasses[x])*100/testClasses[x]))

		# Find the confusion matrix
		for x in xrange(0,len(testLabels)):
			confusionMatrix[testLabels[x]][hypotheticalLabels[x]] += 1

		for x in xrange(0,10):
			for y in xrange(0,10):
				confusionMatrix[x][y] = confusionMatrix[x][y] * 100 / testClasses[x]

		error_value = float(count_nonzero(error))/10
		file = open("sample.txt" , "w")

		for i in xrange(0,10):
			print "Digit Class: ", i
			print "Highest Posterior", classesList[i].highestPosterior
			for x in range(28):
				for y in range(28):
					print classesList[i].highPostImage[x][y],
				print "\n"
			print "Lowest Posterior", classesList[i].lowestPosterior
			for x in range(28):
				for y in range(28):
					print classesList[i].lowPostImage[x][y],
				print "\n"
		#print "The error is ", error_value
		#print "Success Rate: ", int(100-error_value), " for a value of k: ", i

		#print "Classification Rate: ", error_by_class

		#print confusionMatrix
		#print "This is the priors: ",labelsList, " for a smoothing of: ", i
		#print "This is the actual stats: ",testClasses, " for a smoothing of: ", i
		#print "This is the hypothetical stats: ",hypotheticalClasses, " for a smoothing of: ", i
		#print "Error By Digit: ", error_by_class
		#print "This is the likelihood: ", classesList[x].empirical_likelihood


if __name__ == '__main__':
	main()