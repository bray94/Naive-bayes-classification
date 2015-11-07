from numpy import *

def likelihood(list):
	empirical_likelihood = zeros((28,28))
	for x in list:
		empirical_likelihood = add(empirical_likelihood, x)

	return empirical_likelihood/len(list)


def smoothed_likelihood(list, k):	
	empirical_likelihood = zeros((28,28))
	for x in list:
		empirical_likelihood = add(empirical_likelihood, x)

	return (empirical_likelihood+k)/(len(list) + 2*k)


def main():
	print "Hello!"

if __name__ == '__main__':
	main()