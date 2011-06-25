import os
from tables.clicker_grades import ClickerGrades
from tables.remoteID import RemoteID


def grade_class(directory):
    remoteID = RemoteID(os.path.join(directory, 'RemoteID.csv'))
    datadir = os.path.join(directory, 'SessionData')
    outputdir = os.path.join(directory, 'Upload')
    def find_files(name): return name[0]=='L' and name[-3:]=='csv'
    files = filter(find_files, os.listdir(datadir))
    files.sort()
    for i, file in enumerate(files):
        inputname = os.path.join(datadir, file)
        session = ClickerGrades(inputname, remoteID)
        outputname = os.path.join(outputdir, 'Rlqz' + str(i + 1) + '.csv')
        session.output_CHIP(outputname)

if __name__ == '__main__':
    directory = '/home/dsj9/Grades/iclicker Win/Classes/Electrodynamics-241-16'
    grade_class(directory)