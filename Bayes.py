from emailClass import *

def multinomial_reg(classific):
	# number of times word appears in document/ documents in class

	for doc in classific.training_data:

		# for each word in the doc
		for key,value in doc.dictionary.iteritems():
			
			if(key not in classific.m_likelihood_reg):
				counter = 0

				# for each doc in the training data
				for doc in classific.training_data:
					if(key in doc.dictionary):
						counter +=doc.dictionary[key]

				classific.m_likelihood_reg[key] = float(counter)/classific.total_words

def multinomial_spam(classific):
	# number of times word appears in document/ documents in class

	for doc in classific.training_data:

		# for each word in the doc
		for key,value in doc.dictionary.iteritems():
			
			if(key not in classific.m_likelihood_spam):
				counter = 0

				# for each doc in the training data
				for doc in classific.training_data:
					if(key in doc.dictionary):
						counter +=doc.dictionary[key]

				classific.m_likelihood_spam[key] = float(counter)/classific.total_words

def bernouilli_reg(classific):
	# number of documents word appears/ documents in class

	# for every doc in the training data
	for doc in classific.training_data:

		# for each word in the doc
		for key,value in doc.dictionary.iteritems():
			
			if(key not in classific.b_likelihood_reg):
				counter = 0

				# for each doc in the training data
				for doc in classific.training_data:
					if(key in doc.dictionary):
						counter +=1

				classific.b_likelihood_reg[key] = float(counter)/len(classific.training_data)

def bernouilli_spam(classific):
	# number of documents word appears/ documents in class

	# for every doc in the training data
	for doc in classific.training_data:

		# for each word in the doc
		for key,value in doc.dictionary.iteritems():
			
			if(key not in classific.b_likelihood_spam):
				counter = 0

				# for each doc in the training data
				for doc in classific.training_data:
					if(key in doc.dictionary):
						counter +=1

				classific.b_likelihood_spam[key] = float(counter)/len(classific.training_data)


if __name__ == '__main__':
	main()