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
    
    def upload(self, url, section, filename, quizname):
        '''Upload file to CHIP'''
        self.browser.open(url)
#        for form in self.browser.forms():
#            print form
#        page = self.browser.response().read()
        self.browser.select_form(nr=3) #  Section selection form
        self.browser.form['secsel']=[section]
        self.browser.form['stype']=['Recitation quizzes']
#        self.browser.form['extype']=[quizname]
        resp = self.browser.submit(nr=0) #  Click on the first button
#        print(self.browser.response().read())
        #  We are on the section select page
        self.browser.select_form(nr=2)
        self.browser.form['sname']=[quizname]
        resp = self.browser.submit(nr=2)  #  tell it to import character delimited data
        #  We are now on the file selection page
        self.browser.select_form(nr=2)
        self.browser.form.add_file(open(filename), 'text/plain', filename)
        resp = self.browser.submit(nr=0)
        #  We made it to the final upload page
        self.browser.select_form(nr=2) 
        print(self.browser.form)
        self.browser.form['ssnat']='1'
        self.browser.form['gradechars']='4'
        self.browser.form['delim']=[',']
        self.browser.form['more']=['0']
        resp = self.browser.submit(nr=0)
        #  Last page, tell it to import for real
        self.browser.select_form(nr=2)
        resp = self.browser.submit(nr=1)
#        print(self.browser.response().read())
#        print(page)
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
    for i in range(1, 13):
        sample.upload(url_gradebook, 'R06', 
                      '/home/daniel/Dropbox/Physics/Electrodynamics/Physics241/Grades/Section06/Upload/Rlqz{0:02d}.csv'.format(i), 
                      'Rlqz{0:02d}'.format(i))
