from goose import Goose

class ArticleCrawler(object):
	def __init__(self):
		self.goose = Goose()

	# grabs and processes the raw content from an article link
	# into a list of a list of sentences
	def url_content(self, url):
		a = self.goose.extract(url=url)
		u_txt = a.cleaned_text
		txt = u_txt.encode('ascii', 'ignore')
		txt = str(txt.decode('unicode_escape')).encode('utf-8')

		return txt