#!/usr/bin/python
# -*- coding: utf8 -*-

import json, sys, os
import nltk
from newspaper import Article

url = functionName = sys.argv[1]
article = Article(url)
article.download() #Downloads the link’s HTML content
article.parse() #Parse the article
nltk.download('all')#1 time download of the sentence tokenizer
article.nlp()#  Keyword extraction wrapper

data = article.__dict__

print json.dumps(data)