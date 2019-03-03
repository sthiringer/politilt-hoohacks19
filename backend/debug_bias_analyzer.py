from random import random

l_tags = ['cnn.com', 'dailyprogress.com', 'vox.com', 'nytimes.com', 'washingtonpost.com']
c_tags = ['foxnews.com', 'breitbart.com', 'dailywire.com']

SCORE_BREADTH = 2.0
SSCORE_BREADTH = 1.2
class DebugBiasAnalyzer:
	''' Helps to debug our bias analysis frontend code. '''
	def __init__(self):
		self.__cache__ = {}

	def score(self, url):
		if url in self.__cache__:
			return self.__cache__[url]
		for t in l_tags:
			if t in url:
				self.__cache__[url] = -1 * self.__sscore()
				return self.__cache__[url]
		for t in c_tags:
			if t in url:
				self.__cache__[url] = self.__sscore()
				return self.__cache__[url]
		return self.__score()

	def __sscore(self):
		return 1 - random() * SSCORE_BREADTH

	def __score(self):
	    return 1 - random() * SCORE_BREADTH