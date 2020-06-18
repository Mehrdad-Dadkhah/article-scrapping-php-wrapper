#!/usr/bin/python
# -*- coding: utf8 -*-

import json, sys, os
import nltk
from newspaper import Article
from datetime import datetime
import lxml, lxml.html

url = functionName = sys.argv[1]
article = Article(url)
article.download() #Downloads the link’s HTML content
article.parse() #Parse the article
nltk.download('all')#1 time download of the sentence tokenizer
article.nlp()#  Keyword extraction wrapper

data = article.__dict__
del data['config']
del data['extractor']

for i in data:
    if type(data[i]) is set:
        data[i] = list(data[i])
    if type(data[i]) is datetime:
        data[i] = data[i].strftime("%Y-%m-%d %H:%i:%s")
    if type(data[i]) is lxml.html.HtmlElement:
        data[i] = lxml.html.tostring(data[i])
    if type(data[i]) is bytes:
        data[i] = str(data[i])

print(json.dumps(data))