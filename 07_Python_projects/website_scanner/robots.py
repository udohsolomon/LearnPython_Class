import urllib.request
import io

def get_robots(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    req = urllib.request.urlopen(path + 'robots.txt', data=None)
    data = io.TextIOwrapper(req, encoding = 'utf-8')
    return data.read()

print(get_robots('https://www.coventry.ac.uk/'))

