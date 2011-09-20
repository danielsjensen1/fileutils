import mechanize
import re
from BeautifulSoup import BeautifulSoup


class Upload(object):
    def __init__(self, authenticate_url=None):
        #  Set up the browser
        self.browser = mechanize.Browser()
        self.browser.set_handle_equiv(True)
#       self. browser.set_handle_gzip(True)
        self.browser.set_handle_redirect(True)
        self.browser.set_handle_referer(True)
        self.browser.set_handle_robots(False)
        self.browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        self.browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:6.0) Gecko/20100101 Firefox/6.0')]
        if authenticate_url is not None:
            self.authenticate(authenticate_url)
    
    def authenticate(self, authenticate_url):
        self.browser.open(authenticate_url)
        for form in self.browser.forms():
            print form
        self.browser.select_form(nr=0)
        self.browser.form['username'] = raw_input('Enter your username: ')
        self.browser.form['password'] = raw_input('Enter your password: ')
        self.browser.submit()
        print('Authenticated')
    
    def upload(self, url, file):
        '''Upload file to CHIP'''
        self.browser.open(url)
        for form in self.browser.forms():
            print form
        page = self.browser.response().read()
        print(page)
#        soup = BeautifulSoup(page)
#        tags = soup.findAll('a', {'href' : re.compile('\.' + filetype)})
#        print tags
#        for tag in tags:
#            href = tag['href']
#            print href
#    
#            file2dl = urllib2.urlopen(url + href)
#    
#            filename = href.rsplit('/', 1)[-1]
#            output = open(filename, 'wb')
#            output.write(file2dl.read())
#            output.close()
    
    #        urllib2.urlopen(file)


if __name__ == '__main__':
    url_login = 'https://www.purdue.edu/apps/account/cas/login'
    url_gradebook = "https://chip.physics.purdue.edu/cgi-bin/241/fall2011/Instructorgradebook/gbins"
    sample = Upload(url_gradebook)
    sample.upload(url_gradebook, '/tmp/blah')
