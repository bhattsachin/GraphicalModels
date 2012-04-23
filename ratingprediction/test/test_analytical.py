'''
Created on Apr 22, 2012

@author: bhatt
'''
import unittest
from ratingprediction.util.readexcel import FileUtil
from ratingprediction.util.statistics import Statistics
import numpy


class Test(unittest.TestCase):


    def testComputeNDBucketAnalytical1(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,27])
        print "-------------------Analytical 1--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass
    
    def testComputeNDBucketAnalytical2(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,28])
        print "-------------------Analytical 2--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass
    
    def testComputeNDBucketAnalytical3(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBuckets(mat[:,29])
        print "-------------------Analytical 3--------------------------"
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        print "-----------------------------------------------------"
        pass
    



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()