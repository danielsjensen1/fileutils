import os, subprocess


class Convert(object):
    def __init__(self, inputdir=None, outputdir=None):
        if inputdir == None:
            inputdir = os.getcwd()
        os.listdir(inputdir)
