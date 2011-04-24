import unittest
from tables.grading import GradeQuizzes


class TestGrading(unittest.TestCase):


    def test_header(self):
        filename = 'smallclass.csv'
        smallclass = GradeQuizzes(filename)
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_header']
    unittest.main()