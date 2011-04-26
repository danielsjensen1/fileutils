import csv
from os.path import splitext


class ClickerGrades(object):
    def __init__(self, filename, remoteID):
        self.filename = filename
        self.parse_file()

#    char.array([['a','b','c'],['a','c','c'],['b','c','c']])
    def parse_file(self, header=10):
        '''The header has 10 lines of information that we should store in the future.'''
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            self.conversion = []
            for i in range(10): reader.next()
            for row in reader:
                print row
                b=[a[i][0] for i in range(len(a))]
#                new_rows = self.convertID(row)
#                self.conversion.extend(new_rows)

from tables.remoteID import RemoteID
if __name__ == '__main__':
    remoteID_13 = RemoteID('/home/dsj9/Grades/iclicker Win/Classes/Electrodynamics-241-13/RemoteID.csv')
    section13 = ClickerGrades('/home/dsj9/Grades/iclicker Win/Classes/Electrodynamics-241-13/SessionData/L1104131126.csv', remoteID_13)