#!/usr/bin/python
# -*- coding: utf8 -*-

import json, sys, os
import nltk
from newspaper import Article
from datetime import datetime
import lxml, lxml.html

sys.stdout = open(os.devnull, "w") #To prevent a function from printing in the batch console in Python

url = functionName = sys.argv[1]
article = Article(url)
article.download() #Downloads the link’s HTML content
article.parse() #Parse the article
#nltk.download('all')#1 time download of the sentence tokenizer
article.nlp()#  Keyword extraction wrapper

sys.stdout = sys.__stdout__

data = article.__dict__
del data['config']
del data['extractor']

for i in data:
    if type(data[i]) is set:
        data[i] = list(data[i])
    if type(data[i]) is datetime:
        data[i] = data[i].strftime("%Y-%m-%d %H:%M:%S")
    if type(data[i]) is lxml.html.HtmlElement:
        data[i] = lxml.html.tostring(data[i])
    if type(data[i]) is bytes:
        data[i] = str(data[i])

print(json.dumps(data))