from numpy import *

"""
This function computes the likelihood using
Laplace smoothing for a number class object 
based on the test data and the value of the 
smoothing constant
"""
def smoothed_likelihood(list, k):	
	empirical_likelihood = zeros((28,28))
	for x in list:
		empirical_likelihood = add(empirical_likelihood, x)

	return (empirical_likelihood+k)/(len(list) + 2*k)

if __name__ == '__main__':
	main()