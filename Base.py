from numpy import * 
from numberClass import *
from training import *
from testing import *
from Document import *
from emailClass import *
from Bayes import *

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

def part1():
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

		testingImagesList = readTestingImages()
		hypotheticalLabels = []
		confusionMatrix = zeros((10,10))

		for x in xrange(0, len(testingImagesList)):
			hypotheticalLabels.append(numClassifier(classesList,testingImagesList[x]))

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
			print classesList[i].highPostImage
			print "Lowest Posterior", classesList[i].lowestPosterior
			print classesList[i].lowPostImage
		#print "The error is ", error_value
		#print "Success Rate: ", int(100-error_value), " for a value of k: ", i

		#print "Classification Rate: ", error_by_class

		#print confusionMatrix
		#print "This is the priors: ",labelsList, " for a smoothing of: ", i
		#print "This is the actual stats: ",testClasses, " for a smoothing of: ", i
		#print "This is the hypothetical stats: ",hypotheticalClasses, " for a smoothing of: ", i
		#print "Error By Digit: ", error_by_class
		#print "This is the likelihood: ", classesList[x].empirical_likelihood

def readTrainingEmails():

	#Open the training emails
	file = open("spamdata/train_email.txt", "r")

	emails = []
	

	for line in file:

		linelist = line.split()
		dictemails = {}


		for x in xrange(1,len(linelist)):
			a,b = linelist[x].split(":")
			dictemails[a] = int(b) 

		emails.append(Document(labelvalue = int(linelist[0]), dictemails))

	file.close()

	return emails

def readTestingEmails():

	#Open the training emails
	file = open("spamdata/test_email.txt", "r")

	actuallabels = []
	testingemails= []
	

	for line in file:

		linelist = line.split()
		dictemails = {}

		for x in xrange(1,len(linelist)):
			a,b = linelist[x].split(":")
			dictemails[a] = int(b) 

		actuallabels.append(int(linelist[0]))
		testingemails.append(Document(dictemails))

	file.close()

	return actuallabels,testingemails

def part2():
	training_emails = readTrainingEmails()
	spam_emails = []
	reg_emails = []

	for email in training_emails:
		if(email.label == 0):
			reg_emails.append(email)
		else:
			spam_emails.append(email)

	emails_classes = []
	emails_classes.append(emailClass(reg_emails))
	emails_classes.append(emailClass(spam_emails))

	multinomial(emails_classes[0])
	multinomial(emails_classes[1])
	bernouilli(emails_classes[0])
	bernouilli(emails_classes[1])

	# file = open("multinomial_regular.txt", "w")
	# print>>file, emails_classes[0].m_likelihood_reg
	# file.close()

	# file = open("multinomial_spam.txt", "w")
	# print>>file, emails_classes[1].m_likelihood_spam
	# file.close()

	# file = open("bernouilli_regular.txt", "w")
	# print>>file, emails_classes[0].b_likelihood_reg
	# file.close()

	# file = open("bernouilli_spam.txt", "w")
	# print>>file, emails_classes[1].b_likelihood_spam
	# file.close()

	actual_labels, testing_emails = readTestingEmails()







def main():
	part2()

if __name__ == '__main__':
	main()