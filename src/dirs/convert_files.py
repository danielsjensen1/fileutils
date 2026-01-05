import os, subprocess
import shutil


class ConvertFiles(object):
    def __init__(self, inputext, outputext, inputdir, outputdir):
        self.inputext = inputext
        self.outputext = outputext
        if inputdir == None:
            self.inputdir = os.getcwd()
        else:
            self.inputdir = inputdir
        if outputdir == None:
            self.outputdir = os.getcwd()
        else:
            self.outputdir = outputdir
            if not os.path.exists(outputdir):
                try:
                    os.makedirs(outputdir)
                except os.error:
                    print('{} cannot be created'.format(outputdir))
                    raise
        #  We should probably run a check on inputdir to make sure it is normalized
        self.N = len(inputdir) + 1

    def walk(self):
        for root, folders, filenames in os.walk(self.inputdir, topdown=True):
            for folder in folders:
                path = os.path.join(self.outputdir, root[self.N:], folder)
                try:
                    os.mkdir(path)
                except OSError:
                    print('{} already exists'.format(path))
                    #  We may not have permissions to write to this folder
            for filename in filenames:
                name, ext = os.path.splitext(filename)
                ext = ext.lower()
                if ext == self.inputext:
                    inpath = os.path.join(root, filename)
                    outpath = os.path.join(self.outputdir, root[self.N:],
                                       name + self.outputext)
                    yield inpath, outpath



class FlacToOgg(ConvertFiles):
    def __init__(self, inputdir=None, outputdir=None):
        ConvertFiles.__init__(self, '.flac', '.ogg', inputdir, outputdir)

    def __call__(self, quality=5):
        # add support for --quiet flag
        for inpath, outpath in self.walk():
            subprocess.check_call(['oggenc', inpath, '-q {}'.format(quality),
                                   '-o', outpath])


class FlacToMp3(ConvertFiles):
    def __init__(self, inputdir=None, outputdir=None):
        ConvertFiles.__init__(self, '.flac', '.mp3', inputdir, outputdir)

    def __call__(self, quality=0):
        # add support for --quiet flag
        for inpath, outpath in self.walk():
            subprocess.check_call(['ffmpeg', '-i', inpath, '-qscale:a', '{}'.format(quality),
                                   outpath])


class CopyAlbumArt(ConvertFiles):
    def __init__(self, inputdir=None, outputdir=None):
        ConvertFiles.__init__(self, '.jpg', '.jpg', inputdir, outputdir)

    def __call__(self):
        # add support for --quiet flag
        for inpath, outpath in self.walk():
            shutil.copyfile(inpath, outpath)


if __name__ == '__main__':
#    inputdir = os.path.join(os.getcwd(), 'test', 'inputaudio')
#    outputdir = os.path.join(os.getcwd(), 'test', 'outputaudio')
#    converter = FlacToOgg(inputdir, outputdir)
#    converter(quality=3)

    inputdir = '/mnt/entertainment/audio/flac'
    inputdir = os.path.expanduser('~/Music/flac')
    outputdir = os.path.expanduser('~/Music/ogg2')
    converter = FlacToOgg(inputdir, outputdir)
    # converter = FlacToMp3(inputdir, outputdir)
    converter()
    converter = CopyAlbumArt(inputdir, outputdir)
    converter()