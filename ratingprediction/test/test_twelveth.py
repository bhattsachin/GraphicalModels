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
        ndBucket = statistics.computeNDBuckets(mat[:,8])
        
        
        
        for idx,val in enumerate(ndBucket):
            print "bucket#" + str(idx) + " total: " + str(len(val)) + " min: " + str(min(val)) + " max: " + str(max(val))
        pass
    
    
    def testCompareWithPerformance(self):
        fileutil = FileUtil()
        data = fileutil.readFile("../resource/dataset.xls")
        statistics = Statistics()
        mat = numpy.array(data[2:len(data)]);
        ndBucket = statistics.computeNDBucketsWrtPrediction(mat[:,8], mat[:,30])
        
        for idx,val in enumerate(ndBucket):
            total = 0
            for yval in val:
                total = total + len(yval) # waste of n cycles
                
            print "$performer:" + str(idx)
            for fdx, yval in enumerate(val):
                print "probability#" + str(len(yval) / float(total)) + "--  P(" + str(idx) + "|" + str(fdx) + ")"
                print "grade#" + str(fdx) + " total: " + str(len(yval)) + " min: " + str(min(yval)) + " max: " + str(max(yval))
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testComputeNDBucket']
    unittest.main()