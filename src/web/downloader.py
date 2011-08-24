import re
from BeautifulSoup import BeautifulSoup
import urllib2


def download(url, filetype='mp3'):
    '''To-do: add support for proxies'''
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    tags = soup.findAll('a', {'href' : re.compile('\.' + filetype)})
    print tags
    for tag in tags:
        href = tag['href']

        file2dl = urllib2.urlopen(url + href)

        filename = href.rsplit('/', 1)[-1]
        output = open(filename, 'wb')
        output.write(file2dl.read())
        output.close()

#        urllib2.urlopen(file)


if __name__ == '__main__':
    url = "http://www.lds.org/library/display/0,4945,8009-1-4355-37,00.html"
    url = "http://www.physics.purdue.edu/academic_programs/courses/phys221/exam_archive/"
    url = "http://www.springerlink.com.login.ezproxy.lib.purdue.edu/content/978-3-540-35422-2/contents/"
    download(url, 'pdf')
