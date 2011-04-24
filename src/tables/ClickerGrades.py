import csv
from os.path import splitext


class ClickerGrades(object):
    def __init__(self, filename, output=False):
        self.filename = filename
#        if output is True:
#            self.convert_file()
#            self.print_file()
    char.array([['a','b','c'],['a','c','c'],['b','c','c']])
    def parse_file(self, header=10):
        '''The header has 10 lines of information that we should store in the future.'''
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            self.conversion = []
            for row in reader[10:]:
                print row
#                new_rows = self.convertID(row)
#                self.conversion.extend(new_rows)