# -*- coding: utf-8 -*-

from tf.bias_analyzer import BiasAnalyzer
import argparse, pickle, time

################ GET WEB CONTENT ###################
# urls = [
	# 'https://www.nytimes.com/2017/08/02/us/politics/trump-immigration.html', 
	# 'http://www.foxnews.com/politics/2017/08/07/democrats-divided-over-whether-party-should-welcome-pro-life-candidates.html'
	# ]

############## TESTING ARTICLE ANALYSIS ############
def get_bias_from_text(url, text, bias_analyzer, print_sentences=False):
	score, sentence_scores = bias_analyzer.get_article_bias(text)
	print '\nURL:', url, '\n\nScore:', score
	print
	if print_sentences:
		for s in sentence_scores: 
			print s, sentence_scores[s]

def get_liberal_articles():
	return load_pickle('test_corpus/liberal.p')

def get_conservative_articles():
	return load_pickle('test_corpus/conservative.p')

def load_pickle(filename):
	return pickle.load( open(filename, "rb") )

############# SVM TRAINING ##############
'''
analyzer.train_SVM()
print('done')
print(str(time.time() - start_time))
'''
def main():
	# get args
	parser = argparse.ArgumentParser()
	parser.add_argument('--svm', metavar='svm', type=bool, default=False,
	                    help='use SVM for classification')
	parser.add_argument('--print_sentences', metavar='print_sentences', type=bool, default=False,
	                    help='print all sentence_scores')
	args = parser.parse_args()
	# make bias thing
	analyzer = BiasAnalyzer(withSVM=args.svm)
	# do liberal articles
	print '\n\tLiberal test articles:\n'
	for url, text in get_liberal_articles():
		get_bias_from_text(url, text, analyzer)

	print '\n\tConservative test articles:\n'
	for url, text in get_conservative_articles():
		get_bias_from_text(url, analyzer, print_sentences=args.print_sentences)


main()