# article-scrapping-php-wrapper

Simple php wrapper on Newspaper3k Article scraping &amp; curation

[![Software License](https://img.shields.io/badge/license-GPL-brightgreen.svg?style=flat-square)](LICENSE)
[![Packagist Version](https://img.shields.io/packagist/v/Mehrdad-Dadkhah/article-scrapping-php-wrapper.svg?style=flat-square)](https://packagist.org/packages/Mehrdad-Dadkhah/ArticleScrappingPhpWrapper)

## Features

- Multi-threaded article download framework
- News url identification
- Text extraction from html
- Top image extraction from html
- All image extraction from html
- Keyword extraction from text
- Summary extraction from text
- Author extraction from text
- Google trending terms extraction
- Works in 10+ languages (English, Chinese, German, Arabic, ...)

.. code-block:: pycon

    >>> import newspaper
    >>> newspaper.languages()

    Your available languages are:
    input code      full name

      ar              Arabic
      be              Belarusian
      bg              Bulgarian
      da              Danish
      de              German
      el              Greek
      en              English
      es              Spanish
      et              Estonian
      fa              Persian
      fi              Finnish
      fr              French
      he              Hebrew
      hi              Hindi
      hr              Croatian
      hu              Hungarian
      id              Indonesian
      it              Italian
      ja              Japanese
      ko              Korean
      lt              Lithuanian
      mk              Macedonian
      nb              Norwegian (Bokmål)
      nl              Dutch
      no              Norwegian
      pl              Polish
      pt              Portuguese
      ro              Romanian
      ru              Russian
      sl              Slovenian
      sr              Serbian
      sv              Swedish
      sw              Swahili
      th              Thai
      tr              Turkish
      uk              Ukrainian
      vi              Vietnamese
      zh              Chinese

## Get it now

Run ✅ `pip3 install newspaper3k` ✅

NOT ⛔ `pip3 install newspaper` ⛔

On python3 you must install `newspaper3k`, **not** `newspaper`. `newspaper` is our python2 library.
Although installing newspaper is simple with `pip <http://www.pip-installer.org/>`\_, you will
run into fixable issues if you are trying to install on ubuntu.

**If you are on Debian / Ubuntu**, install using the following:

- Install `pip3` command needed to install `newspaper3k` package::

  \$ sudo apt-get install python3-pip

- Python development version, needed for Python.h::

  \$ sudo apt-get install python-dev

- lxml requirements::

  \$ sudo apt-get install libxml2-dev libxslt-dev

- For PIL to recognize .jpg images::

  \$ sudo apt-get install libjpeg-dev zlib1g-dev libpng12-dev

NOTE: If you find problem installing `libpng12-dev`, try installing `libpng-dev`.

- Download NLP related corpora::

  \$ curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3

- Install the distribution via pip::

  \$ pip3 install newspaper3k

**If you are on OSX**, install using the following, you may use both homebrew or macports:

::

    $ brew install libxml2 libxslt

    $ brew install libtiff libjpeg webp little-cms2

    $ pip3 install newspaper3k

    $ curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3

**Otherwise**, install with the following:

NOTE: You will still most likely need to install the following libraries via your package manager

- PIL: `libjpeg-dev` `zlib1g-dev` `libpng12-dev`
- lxml: `libxml2-dev` `libxslt-dev`
- Python Development version: `python-dev`

::

    $ pip3 install newspaper3k

    $ curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3

## Installation

```
composer require mehrdad-dadkhah/article-scrapping-php-wrapper
```

## Usage

```PHP
use MehrdadDadkhah\Scrapp\ArticleScrappingWrapper;

$parser = new ArticleScrappingWrapper();

$parser->scrapp('your url');
```

## Read more

(Newspaper)[https://github.com/codelucas/newspaper]

(nltk)[http://www.nltk.org/install.html]

(Scrape & Summarize News Articles Using Python)[https://medium.com/@randerson112358/scrape-summarize-news-articles-using-python-51a48af1b4e2]

(Corpora Iranian Persian)[https://wortschatz.uni-leipzig.de/en/download/iranian-persian]
