# -*- coding: utf-8 -*-

from tf.bias_analyzer import BiasAnalyzer
from article_crawler import ArticleCrawler
import time
import cPickle

print('if this breaks, remember to add the tf folder to PYTHONPATH and try again')

################ GET WEB CONTENT ###################
urls = [
	'https://www.nytimes.com/2017/08/02/us/politics/trump-immigration.html', 
	'http://www.foxnews.com/politics/2017/08/07/democrats-divided-over-whether-party-should-welcome-pro-life-candidates.html'
	]
crawler = ArticleCrawler()

paragraphs = {}
for url in urls:
	paragraphs[url] = crawler.url_content(url)

############## INITIALIZING ANALYZER ###############
print('initializing bias analyzer')
start_time = time.time()
#analyzer = BiasAnalyzer()
analyzer = BiasAnalyzer(withSVM=False) # SVM?
print('done')
print(str(time.time() - start_time))

start_time = time.time()

############## TESTING ARTICLE ANALYSIS ############
totalbias = {}
totaldict = {}
for url in urls:
	a = analyzer.get_article_bias(paragraphs[url])
	print('a:',a)
	totalbias[url], totaldict[url] = a
print('done getting bias')
print(str(time.time() - start_time))
for url in urls:
	print()
	print('article url: ', url)
	print('total bias index for the entire article', totalbias[url])
	print('total dict:', totaldict[url])

############# SVM TRAINING ##############
'''
analyzer.train_SVM()
print('done')
print(str(time.time() - start_time))
'''