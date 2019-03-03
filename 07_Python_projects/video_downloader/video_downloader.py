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

def get_links():

    # create response object
    r = requests.get(archive_url)
    # create Beautiful soup object
    soup bs(r.content, 'html5lib')
    # find all links on the web page
    links = soup.findAll('a')
    # filter the links sending with .mp4
    video_links = [archive_url + links['href'] for link in links if link['href'].endswith('mp4')]
    return video_links