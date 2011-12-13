import csv
from os.path import splitext


class RemoteID(object):
    def __init__(self, filename):
        self.filename = filename
        self.id_map = {}
        self.convert_file()
#        self.print_file()
    
    def convert_file(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            self.conversion = []
            for row in reader:
                new_rows = self.convertID(row)
                self.conversion.extend(new_rows)
        print self.id_map
    
    
    def convertID(self, row):
        mappedIDs = {}
#        data = student.split(',')
#        studentID = '"' + data[1] + '"'
        studentID = row[1]
        #  You used to need to strip the leading zeros but not with the new version
#        self.id_map['#' + row[0].lstrip('0')] = studentID
        self.id_map['#' + row[0]] = studentID
#        rows.append('#' + data[0] + ',' + studentID)
#        rows.append(data[0] + ',' + studentID)
        try:
            extraIDs = row[5].split(' ')
            for extraID in extraIDs:
#                rows.append('#' + extraID + ',' + studentID)
#                self.id_map['#' + extraID.lstrip('0')] = studentID
                self.id_map['#' + extraID] = studentID
        except IndexError:
            #  It is OK if there aren't extra ID numbers
            pass
        return mappedIDs
    
    def print_file(self):
        outputfilename = self.filename + '.converted'
        with open(outputfilename, 'wb') as f:
            for line in self.conversion:
                f.write(line + '\n')
    
if __name__ == '__main__':
    filename13 = '/home/dsj9/Grades/iclicker Win/Classes/Electrodynamics-241-13/SessionData/webRemoteID.csv'
    section13 = RemoteID(filename13, output=True)