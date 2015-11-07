from numpy import * 
from numberClass import *
from training import *
from testing import *

classes = (10)


def readTrainingLabels():
	# Open The File
	file = open("digitdata/traininglabels.txt" , "r")

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
	file = open("digitdata/trainingimages.txt", "r")

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
	file = open("digitdata/testlabels.txt" , "r")

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
	file = open("digitdata/testimages.txt", "r")

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

	for i in xrange(0,1):
		for x in xrange(0,10):
			classesList[x].empirical_likelihood = smoothed_likelihood(classesList[x].training_data,i)

		testingImagesList = readTestingImages()
		hypotheticalLabels = []

		for x in xrange(0, len(testingImagesList)):
			hypotheticalLabels.append(numClassifier(classesList,testingImagesList[x]))

		hypotheticalClasses = [0,0,0,0,0,0,0,0,0,0]
		for element in hypotheticalLabels:
			hypotheticalClasses[element]+=1

		print hypotheticalClasses
		
		testClasses, testLabels = readTestingLabels()

		error = list(array(hypotheticalLabels) - array(testLabels))

		error_by_class = []
		for x in xrange(0,10):
			error_by_class.append(abs(float(hypotheticalClasses[x]-testClasses[x])/testClasses[x]))



		error_value = float(count_nonzero(error))/1000

	
		print "This is the priors: ",labelsList, " for a smoothing of: ", i
		print "This is the actual stats: ",testClasses, " for a smoothing of: ", i
		print "This is the hypothetical stats: ",hypotheticalClasses, " for a smoothing of: ", i


if __name__ == '__main__':
	main()