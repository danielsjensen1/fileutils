from clicker_grades import ClickerGrades


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


from remoteID import RemoteID
from os.path import join
if __name__ == '__main__':
#    grading = '/home/jensend/Dropbox/Physics/Electrodynamics/Giordano/Recitations/Grades/clicker'
    grading = '/home/daniel/Dropbox/Physics/Electrodynamics/Giordano/Recitations/Grades/clicker'
    remoteID = RemoteID(join(grading, 'RemoteID.csv'))
    quizzes = (('L1106211049.csv', 'BCC', (2,1,2), 'upload03.csv'),
               ('L1106231051.csv', 'CCCD', (1,1,1,2), 'upload04.csv'),
               ('L1106281050.csv', 'BBA', (2,1,2), 'upload05.csv'),
               ('L1106301049.csv', 'CBB', (1,2,2), 'upload06.csv'),
               ('L1107121044.csv', 'ACBC', (1,1,1,2), 'upload07.csv'),
               ('L1107141050.csv', 'C', (5,), 'upload08.csv'),
               ('L1107191045.csv', 'CCD', (2,1,2), 'upload09.csv'),
               ('L1107211045.csv', 'BAA', (2,2,1), 'upload10.csv'),
               ('L1107261049.csv', 'CDAB', (1,1,1,2), 'upload11.csv'),
               ('L1107281050.csv', 'ACD', (2,1,2), 'upload12.csv'))
    for quiz in quizzes:
        filename, key, scoring, upfilename = quiz
        clicker = ClickerWithKey(join(grading, filename), remoteID)
        clicker.grade(key, scoring)
        clicker.output_CHIP(join(grading, upfilename))
#    quiz03 = ClickerWithKey(join(grading, 'L1106211049.csv'), remoteID)
#    quiz03.grade('BCC', (2,1,2))
#    quiz03.output_CHIP(join(grading, 'upload03.csv'))
#    quiz04 = ClickerWithKey(join(grading, 'L1106231051.csv'), remoteID)
#    quiz04.grade('CCCD', (1,1,1,2))
#    quiz04.output_CHIP(join(grading, 'upload04.csv'))
#    quiz05 = ClickerWithKey(join(grading, 'L1106281050.csv'), remoteID)
#    quiz05.grade('BBA', (2,1,2))
#    quiz05.output_CHIP(join(grading, 'upload05.csv'))