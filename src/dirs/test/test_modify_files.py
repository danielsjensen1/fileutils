import unittest
from dirs.modify_files import ghostscript
from os import listdir
from os.path import join
from shutil import copytree, rmtree


class TestGhostscript(unittest.TestCase):
    """
    Test the Ghostscript interface.
    
    Notes
    -----
    Some of these methods are destructive so we create a temporary directory
    containing the files to be processed and then remove it on exit.
    """
    def setUp(self):
        """
        Create a temporary PDF directory for the tests since some of them
        are destructive.
        """
        directory = 'inputpdfs_tmp'
        copytree('inputpdfs', directory)
        filenames = [join(directory, filename) 
                     for filename in listdir(directory)]
        filenames.sort()
        self.directory, self.filenames = directory, filenames
    
    def tearDown(self):
        """Remove the temporary directory created during setup."""
        rmtree(self.directory)
    
    def test_combine(self):
        directory, filenames = self.directory, self.filenames
        ghostscript(filenames, combine=True)
    
    def test_replace_false(self):
        directory, filenames = self.directory, self.filenames
        ghostscript(filenames, combine=False, replace=False)
    
    def test_replace_true(self):
        directory, filenames = self.directory, self.filenames
        ghostscript(filenames, combine=False, replace=True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()