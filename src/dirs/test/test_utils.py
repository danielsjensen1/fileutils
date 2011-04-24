'''
This could use a lot more work to test that good directories/files
aren't deleted along with the bad ones.

@author: dsj9
'''
import os
import os.path
from shutil import rmtree
from dirs.utils import rrmdirs
import unittest


class RecursivelyRemoveFolders(unittest.TestCase):


    def setUp(self):
        """Create some typical svn files and non-svn files."""
        
        self.testdir = os.getcwd()
        self.tmpdir = 'tempdir'
        if os.path.exists(os.path.join(self.testdir, self.tmpdir)):
            rmtree(self.tmpdir)
        os.mkdir(self.tmpdir)
        os.chdir(self.tmpdir)
        folders = ('nonsvn1', 'nonsvn2', '.nonsvn1', '.svn')
        for folder in folders:
            os.mkdir(folder)
        #  Change directory
        os.chdir('.svn')
        svnfolders = ('prop-base', 'props', 'text-base')
        for dir in svnfolders:
            os.mkdir(dir)
        f = open('entries', 'w')
        f.write('Some test words')
        f.close()
        os.chdir(self.testdir)


    def tearDown(self):
        """Remove the temporary directory."""
        os.chdir(self.testdir)
        rmtree('tempdir')


    def test_rmsvn(self):
        """Check that bad folders are removed and good ones remain."""
        rrmdirs('.svn')
        for root, dirs, files in os.walk(self.testdir, topdown=False):
            for dir in dirs:
                self.assertNotEquals(dir, '.svn')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()