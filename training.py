from numpy import *

def likelihood(list):
	empirical_likelihood = zeros((28,28))
	for x in list:
		empirical_likelihood = add(empirical_likelihood, x)

	return empirical_likelihood/list.len()


def smoothed_likelihood(list, k):	
	empirical_likelihood = zeros((28,28))
	for x in list:
		empirical_likelihood = add(empirical_likelihood, x)

	return (empirical_likelihood+k)/(list.len() + 2*k)


def main():
	print "Hello!"
	print "I want to create a new branch"

if __name__ == '__main__':
	main()