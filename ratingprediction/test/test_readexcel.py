'''
Created on Apr 14, 2012

@author: bhatt
'''
from ratingprediction.util.readexcel import FileUtil
import unittest

class Test(unittest.TestCase):


    def testName(self):
        pass
    
    def testReadFile(self):
        #this was dummy
        #self.assertEqual(10,math.log10(100),"OK")
        fileutil = FileUtil()
        fileutil.readFile("../resource/dataset.xls")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()