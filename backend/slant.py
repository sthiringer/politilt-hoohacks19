from goose3 import Goose

raw_html = #Raw html from chrome extension HTTP request goes here


g = Goose()
article = g.extract(raw_html=raw_html)

#### Now extract info with ####

#print(article.title)

#print(article.cleaned_text)

#print(article.meta_description)

