'''
Created on Apr 22, 2012

@author: bhatt
'''
from ratingprediction.util.readexcel import FileUtil
from ratingprediction.util.statistics import Statistics
import numpy
import unittest


class Test(unittest.TestCase):


    def testComputeNDBucket(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,13])
        
        
        print "-------------------Marks obtained by students in college--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()