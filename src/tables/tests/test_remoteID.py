import unittest
import StringIO
from tables.remoteID import RemoteID


class TestRemoteID(unittest.TestCase):

    student1 = ['1ECD67B4', '0022716310', 'Taeyong', 'Ahn', 'tahn',
                '3ECD6794 5ECD67F4 9ECD6734']
    ans1 = {'#3ECD6794': '0022716310', '#1ECD67B4': '0022716310', 
            '#5ECD67F4': '0022716310', '#9ECD6734': '0022716310'}
    def test_convertID(self):
        conversion = RemoteID.convertID(self.student1)
        self.assertEqual(conversion, self.ans1)
    
    ans2 = ['#1ECD67B4,"0022716310"', '#3ECD6794,"0022716310"', 
            '#5ECD67F4,"0022716310"', '#9ECD6734,"0022716310"',
            '#07DDA973,"0022768127"', '#27DDA953,"0022768127"',
            '#47DDA933,"0022768127"', '#87DDA9F3,"0022768127"',
            '#1F37C0E8,"0022768127"', '#3F37C0C8,"0022768127"',
            '#5F37C0A8,"0022768127"', '#9F37C068,"0022768127"']
    def test_small_file(self):
        small_class = RemoteID('smallremoteID.csv')
        small_class.convert_file()
        print small_class.conversion
        self.assertEqual(small_class.conversion, self.ans2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_header']
    unittest.main()