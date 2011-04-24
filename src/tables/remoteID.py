import csv
from os.path import splitext


class RemoteID(object):
    def __init__(self, filename, output=False):
        self.filename = filename
        if output is True:
            self.convert_file()
            self.print_file()
    
    def convert_file(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            self.conversion = []
            for row in reader:
                new_rows = self.convertID(row)
                self.conversion.extend(new_rows)
    
    @classmethod
    def convertID(self, data):
        rows = []
#        data = student.split(',')
#        studentID = '"' + data[1] + '"'
        studentID = data[1]
        rows.append('#' + data[0] + ',' + studentID)
        rows.append(data[0] + ',' + studentID)
        try:
            extraIDs = data[5].split(' ')
            for extraID in extraIDs:
                rows.append('#' + extraID + ',' + studentID)
        except IndexError:
            #  It is OK if there aren't extra ID numbers
            pass
        return rows
    
    def print_file(self):
        outputfilename = self.filename + '.converted'
        with open(outputfilename, 'wb') as f:
            for line in self.conversion:
                f.write(line + '\n')
    
if __name__ == '__main__':
    filename13 = '/home/dsj9/Grades/iclicker Win/Classes/Electrodynamics-241-13/SessionData/webRemoteID.csv'
    section13 = RemoteID(filename13, output=True)