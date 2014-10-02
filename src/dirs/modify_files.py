from subprocess import call
from os.path import splitext
from os import rename, remove


def ghostscript(filenames, combine=False, name='finished.pdf', replace=False):
    """
    Process one or more files using Ghostscript.  
    
    Notes
    -----
    Currently all filenames must end with the '.pdf' extension to be processed
    correctly.
    
    Parameters
    ----------
    files : List or tuple of strings
        The filename(s) to be processed.  
    combine : bool, optional
        Tells Ghostscript to combine all of the PDFs into one file.
    name : string
        Filename of the combined files if combine=True
    replace : bool, optional
        Removes the old files and renames the new files with the old filenames.
        This option has no effect when `combine`=True.
    """
    filenames = list(filenames)
    if combine == True:
        command = ['gs', '-dBATCH', '-dNOPAUSE', '-q', '-sDEVICE=pdfwrite']
        command.append('-sOutputFile={}'.format(name))
        command.extend(filenames)
        print command
        retcode = call(command)
    else:
        for filename in filenames:
            command = ['gs', '-dBATCH', '-dNOPAUSE', '-q', '-sDEVICE=pdfwrite']
            prefix, extension = splitext(filename)
            temp_filename = ''.join([prefix, '_new', extension])
            command.extend(['-sOutputFile={}'.format(temp_filename), filename])
            print command
            retcode = call(command)
            if replace and retcode == 0:
                remove(filename)
                rename(temp_filename, filename)
#     gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=finished.pdf prob02.pdf