import requests
from bs4 import BeautifulSoup as bs

'''
URL of the archive web-page which provides link to
all video lectures. It would have been tiring to
download each video manually.
In this example, we first crawl the webpage to extract
all the links and then download videos.
'''
# specify the url of the link here
archive_url = "http://www-personal.umich.edu/~csev/books/py4inf/media/"