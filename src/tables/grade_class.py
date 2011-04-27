from os.path import splitext
from tables.clicker_grades import ClickerGrades
from tables.remoteID import RemoteID


def grade_class(directory):
    remoteID = RemoteID()

if __name__ == '__main__':
    directory = '/home/dsj9/Grades/iclicker Win/Classes/Electrodynamics-241-13'
    remoteID_13 = RemoteID('/home/dsj9/Grades/iclicker Win/Classes/Electrodynamics-241-13/RemoteID.csv')
    section13 = ClickerGrades('/home/dsj9/Grades/iclicker Win/Classes/Electrodynamics-241-13/SessionData/L1104201126.csv', remoteID_13)