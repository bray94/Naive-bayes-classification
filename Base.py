from numpy import *

def readTrainingLabels():
	# Open The File
	file = open("digitdata/traininglabels.txt" , "r")

	# Count each digit in training set
	list = [0,0,0,0,0,0,0,0,0,0]

	# Total num of digits
	counter = 0

	for line in file:
		list[int(line.strip())]+=1
		counter+=1

	file.close()

	return list

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



def main():
	#priorList = readTrainingLabels()
	imagesList = readTrainingImages()

	#print(priorList)
	#print(imagesList)
	file = open("digitdata/trainingimages_out.txt", "w")

	#for item in imagesList:
	#	print>>file, item

if __name__ == '__main__':
	main()