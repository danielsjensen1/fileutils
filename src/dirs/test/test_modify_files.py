import unittest
from dirs.modify_files import ghostscript
from os import listdir
from os.path import join


class TestGhostscript(unittest.TestCase):
    """
    Test the Ghostscript interface.
    
    Notes
    -----
    Some of these methods are destructive so we create a temporary directory
    containing the files to be processed and then remove it on exit.
    """

    def test_combine(self):
        directory = 'inputpdfs'
        filenames = [join(directory, filename) 
                     for filename in listdir('inputpdfs')]
        filenames.sort()
        ghostscript(filenames, combine=True)
    
    def test_replace_true(self):
        directory = 'inputpdfs'
        filenames = [join(directory, filename) 
                     for filename in listdir(directory)]
        filenames.sort()
        ghostscript(filenames, combine=False, replace=True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()