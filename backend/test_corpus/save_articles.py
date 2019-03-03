''' grabs articles from online and pickles them'''
import pickle
from goose import Goose
from selenium import webdriver

goose = Goose()
options = webdriver.ChromeOptions()
options.add_argument('headless')
client = webdriver.Chrome(options=options)


def grab_articles(article_urls):
	texts = []
	for url in article_urls:
		client.get(url)
		article = goose.extract(raw_html=client.page_source)
		text = article.cleaned_text
		print('URL:',url,'got:',text[:20]+'... ({})'.format(len(text)))
		texts.append((url, text))
	return texts


filenames = ['conservative', 'liberal']
for filename in filenames:
	print (filename)
	urls = open(filename + '.txt').readlines()
	arts = grab_articles(urls)
	pickle.dump(arts, open(filename + '.p', 'wb'), protocol=2)