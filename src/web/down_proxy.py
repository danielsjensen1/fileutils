import mechanize
import re
from BeautifulSoup import BeautifulSoup
import urllib2


def download(url, filetype='pdf'):
    '''Download through ezproxy'''
    browser = mechanize.Browser()
    browser.set_handle_equiv(True)
#    browser.set_handle_gzip(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(False)
    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:6.0) Gecko/20100101 Firefox/6.0')]
    browser.open('https://login.ezproxy.lib.purdue.edu/login')
    browser.select_form(nr=0)
    browser.form['user'] = ''
    browser.form['pass'] = ''
    browser.submit()
    browser.open(url)
    page = browser.response().read()
    soup = BeautifulSoup(page)
    tags = soup.findAll('a', {'href' : re.compile('\.' + filetype)})
    print tags
    for tag in tags:
        href = tag['href']
        print href

#        file2dl = urllib2.urlopen(url + href)
#
#        filename = href.rsplit('/', 1)[-1]
#        output = open(filename, 'wb')
#        output.write(file2dl.read())
#        output.close()

#        urllib2.urlopen(file)


if __name__ == '__main__':
    url = "http://www.springerlink.com.login.ezproxy.lib.purdue.edu/content/978-3-540-35422-2/contents/"
    download(url, 'pdf')
