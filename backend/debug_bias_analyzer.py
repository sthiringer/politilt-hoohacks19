from time import sleep
from random import random

l_tags = ['cnn.com', 'dailyprogress.com', 'vox.com', 'nytimes.com', 'washingtonpost.com']
c_tags = ['foxnews.com', 'breitbart.com', 'dailywire.com']

SCORE_BREADTH = 2.0
SSCORE_BREADTH = 1.2
class DebugBiasAnalyzer:
    ''' Helps to debug our bias analysis frontend code. '''

    def score(self, url):
    	sleep(random() * 2)
        for t in l_tags:
            if t in url:
                return -1 * self.__sscore()
        for t in c_tags:
            if t in url:
                return self.__sscore()
        return self.__score()

    def __sscore(self):
        return self.__unif(SSCORE_BREADTH)

    def __score(self):
        return self.__unif(SCORE_BREADTH)

    def __unif(self, USCALE):
        return 1 - random() * USCALE