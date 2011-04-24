import re
from BeautifulSoup import BeautifulSoup
import urllib2


def download(url, filetype='mp3'):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    tags = soup.findAll('a', {'href' : re.compile('\.mp3')})
    for tag in tags:
        href = tag['href']
        
        file2dl = urllib2.urlopen(href)
        
        filename = href.rsplit('/', 1)[-1]
        output = open(filename, 'wb')
        output.write(file2dl.read())
        output.close()
        
#        urllib2.urlopen(file)
    
    
if __name__ == '__main__':
    url = "http://www.lds.org/library/display/0,4945,8009-1-4355-37,00.html"
    download(url)