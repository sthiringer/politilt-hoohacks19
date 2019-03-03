# -*- coding: utf-8 -*-

from tf.bias_analyzer import BiasAnalyzer
from article_crawler import ArticleCrawler
import time
import argparse

################ GET WEB CONTENT ###################
# urls = [
	# 'https://www.nytimes.com/2017/08/02/us/politics/trump-immigration.html', 
	# 'http://www.foxnews.com/politics/2017/08/07/democrats-divided-over-whether-party-should-welcome-pro-life-candidates.html'
	# ]

############## TESTING ARTICLE ANALYSIS ############
def get_bias_for_url(url, bias_analyzer, article_crawler):
	url = url.replace("'", "")
	text = article_crawler.url_content(url)
	score, sentence_scores = bias_analyzer.get_article_bias(text)
	print '\nURL:', url, '\n\nScore:', score
	print
	for s in sentence_scores: print s, sentence_scores[s]

############# SVM TRAINING ##############
'''
analyzer.train_SVM()
print('done')
print(str(time.time() - start_time))
'''
def main():
	# get args
	parser = argparse.ArgumentParser()
	parser.add_argument('url', metavar='url', type=str,
	                    help='a url to parse')
	parser.add_argument('--svm', metavar='svm', type=bool, default=False,
	                    help='use SVM for classification')
	args = parser.parse_args()
	# make crawler
	crawler = ArticleCrawler()
	# make bias thing
	analyzer = BiasAnalyzer(withSVM=args.svm)
	# get bias
	get_bias_for_url(args.url, analyzer, crawler)

main()