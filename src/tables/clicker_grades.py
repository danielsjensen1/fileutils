import csv


class ClickerGrades(object):
    def __init__(self, filename, remoteID):
        self.filename = filename
        self.id_map = remoteID.id_map
        self.parse_file()
        self.majority_key()
        self.grade()
        
    def grade(self, max_score=3):
        '''This should become a function instead of a loop.'''
        self.final_score = []
        for student, answers in self.responses:
            score = min(max_score, sum(i == j for i, j in zip(answers, self.key)))
            print student, score
            self.final_score.append((student, score))
                    
    def output_CHIP(self, filename):
        with open(filename, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(self.final_score)


    def parse_file(self, header=5):
        '''This is a horribly inefficient method that should be replaced with a database.'''
        with open(self.filename, 'r') as f:
            self.responses = []
            reader = csv.reader(f)
            self.conversion = []
            for i in range(header): reader.next()
            for row in reader:
                try:
#                    print(self.id_map[row[0]] + row[3:-1:6])
                    self.responses.append([self.id_map[row[0]], row[3:-1:6]])
                except KeyError:
                    print row[0], 'not recorded'
                    #  It is OK if the student isn't in the class
                    pass
        print self.responses
    def majority_key(self):
        """The majority rules so the correct answer is the most common answer."""
        def correct_answer(answers):
            possibilities = list('ABCDE')
            counts = map(answers.count, possibilities)
            return possibilities[counts.index(max(counts))]
        answers = zip(*zip(*self.responses)[1])
        self.key = map(correct_answer, answers)
        
#                responses.append(row[0])
#                b=[a[i][0] for i in range(len(a))]
#                new_rows = self.convertID(row)
#                self.conversion.extend(new_rows)

from remoteID import RemoteID
if __name__ == '__main__':
    remoteID_13 = RemoteID('/home/dsj9/Grades/iclicker Win/Classes/Electrodynamics-241-13/RemoteID.csv')
    section13 = ClickerGrades('/home/dsj9/Grades/iclicker Win/Classes/Electrodynamics-241-13/SessionData/L1104201126.csv', remoteID_13)