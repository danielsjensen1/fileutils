import csv
from os.path import splitext


class GradeQuizzes(object):
    normalizer = {'A' : 0.6, 'B': 0.28, 'C':0.12}
    def __init__(self, filename):
        self.reader = csv.reader(open(filename, 'r'))
        self.graded = []
        self.parse_header()
        self.compute_scores()
        print self.graded
        name, ext = splitext(filename)
        outname = name + 'graded' + ext
        writer = csv.writer(open(outname, "wb"))
        writer.writerows(self.graded)
        
    def parse_header(self):
        row = self.reader.next()
        #  Keep the titles of the the first four columns
        newrow = row[0:4]
        #  Add one column for the letter grade
        newrow.append('Grade')
#        newrow.append([str.split('|')[0] for str in row[4:]])
        self.maxscores = [float(str.split('|')[1]) for str in row[4:]]
        self.graded.append(newrow)
        print self.graded
        
    def compute_scores(self, numdropped=3, maxpoints=150):
        total_scores = []
        for row in self.reader:
            #  Store the name (first two columns) and the user id (third column)
            newrow = row[0:3]
            def f(x):
                if len(x) > 0:
                    return float(x)
                else:
                    return 0e0
            scores = [f(x) for x in row[4:]]
            #  Make all scores the same weight (each day is worth the same)
            equalize = [x/y for (x, y) in zip(scores, self.maxscores)]
            #  Sort (low to high) and remove the 'numdropped' lowest values
            equalize.sort()
            del equalize[0:numdropped]
            #  Compute the total score based on the maximum possible points
            numscores = float(len(equalize))
            total_score = maxpoints * sum(equalize) / numscores
            newrow.append(total_score)
            self.graded.append(newrow)
            #  Save the total score in a separate list to assign letter grades
            total_scores.append(total_score)
        def by_score(a):
            return a[3]
        self.graded.sort(key=by_score, reverse=True)
        #  Assign letter grade
#        total_scores.sort()
#        numstudents = len(total_scores)
#        index = int(self.normalizer['A'] * numstudents) + 1
#        A_cutoff = total_scores[index]
#        index = int((self.normalizer['A'] + self.normalizer['B']) * numstudents) + 1
#        B_cutoff = total_scores[index]
#        print A_cutoff, B_cutoff
        
if __name__ == '__main__':
    filename = '/home/dsj9/Dropbox/Physics/Electrodynamics/Physics241/Code/Grades/Section014.csv'
    section = GradeQuizzes(filename)