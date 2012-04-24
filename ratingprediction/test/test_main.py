'''
Created on Apr 23, 2012

@author: bhatt
'''
from ratingprediction.run.main import Main
import unittest

class Test(unittest.TestCase):


    def testMain(self):
        main = Main()
        main.computeFullDataGrades();
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMain']
    unittest.main()
