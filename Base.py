

def readTrainingLabels():
	file = open("digitdata/traininglabels" , "r")

	list = [0,0,0,0,0,0,0,0,0,0]

	counter = 0

	for line in file:
		list[int(line.strip())]+=1
		counter+=1

	file.close()

	return [float(x)/counter for x in list]


def main():
	prior = readTrainingLabels()



if __name__ == '__main__':
	main()