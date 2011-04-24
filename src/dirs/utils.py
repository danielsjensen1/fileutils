import os
from os.path import join
from shutil import rmtree


def rrmdirs(dirname, basedir=None):
    '''
    Recursively remove directories.
    
    If basedir=None then the current working directory is assumed.
    '''
    if basedir is None:
        basedir = os.getcwd()
    for root, dirs, files in os.walk(basedir, topdown=False):
        if dirname in dirs:
            rmtree(join(root, dirname))