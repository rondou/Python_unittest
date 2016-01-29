import unittest

from Codility import *
class test_myUnitTest(unittest.TestCase):

    def setUp(self):
        print "****setUP****"
        print "This will only run once when start-up the test program"
        print "setUP is normally used to prepare testing data/env"

    def test_case1(self):
        print "****test case 1P****"
        print "this is tesitng case 1"
        self.assertEqual (solution([1]), 6)
        self.assertEqual (solution([1,2,3,4]), 13305600)
        self.assertEqual (solution([4,3,2,1]), 13305600)

    def test_case2(self):
        print "****test case 2****"
        print "this is tesitng case 2"
        self.assertEqual(calculator(), 49)
        self.assertEqual(calculator(100, 10000), 188446)

    def tearDown(self):
        print "****tear down****"
        print "This will only run once while closing the test program"
        print "tearDown is normally used to release/close system resource or rollback testing data"
if __name__ == '__main__':
    unittest.main()