from tables.clicker_grades import ClickerGrades


class ClickerWithKey(ClickerGrades):
    def __init__(self, filename, remoteID):
        self.filename = filename
        self.id_map = remoteID.id_map
        self.parse_file()
        
    def grade(self, answer_key, point_value, max_score=5):
        '''This should become a function instead of a loop.'''
        self.final_score = []
        for student, answers in self.responses:
            score = sum((i == j) * k for i, j, k in zip(answers, answer_key,
                                                        point_value))
            score = min(max_score, score)
            print student, score
            self.final_score.append((student, score))


from tables.remoteID import RemoteID
from os.path import join
if __name__ == '__main__':
    grading = '/home/dsj9/Dropbox/Physics/Electrodynamics/Giordano/Recitations/Grades/clicker'
    remoteID = RemoteID(join(grading, 'RemoteID.csv'))
    quiz03 = ClickerWithKey(join(grading, 'L1106211049.csv'), remoteID)
    quiz03.grade('BCC', (2,1,2))
    quiz03.output_CHIP(join(grading, 'upload03.csv'))
#    quiz04 = ClickerWithKey(join(grading, 'L1106231051.csv'), remoteID)
#    quiz04.grade('CCCD', (1,1,1,2))
#    quiz04.output_CHIP(join(grading, 'upload04.csv'))